# custom_storage.py
from django.core.files.storage import Storage
import os
from datetime import datetime

class CustomStorage(Storage):
    def __init__(self, location=None, base_url=None):
        self.location = location or 'media'
        self.base_url = base_url or '/media/'

    def _save(self, file_name, content):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        name = f"{timestamp}_{file_name}"

        if not os.path.exists(self.location):
            os.mkdir(self.location)

        path = None
        if not os.path.exists(os.path.join(self.location, file_name)):
            path = os.path.join(self.location, file_name)
        else:
            path = os.path.join(self.location, name)

        print(path)

        with open(path, "wb") as f:
            for chunk in content.chunks():
                f.write(chunk)        
        return name


    def delete(self, name):
        file_path = os.path.join(self.location, name)
        if os.path.exists(file_path):
            os.remove(file_path)

    def exists(self, name):
        file_path = os.path.join(self.location, name)
        return os.path.exists(file_path)

    def url(self, name):
        return os.path.join(self.base_url, name)

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            base_name, extension = os.path.splitext(name)
            name = f"{base_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{extension}"
        return name

