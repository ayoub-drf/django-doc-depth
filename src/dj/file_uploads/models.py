from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="/media/uploads")

class FileUploadsClass(models.Model):
    img = models.ImageField(upload_to="images/")
    file = models.FileField(upload_to="files/")

    file_2 = models.FileField(storage=fs, null=True,)