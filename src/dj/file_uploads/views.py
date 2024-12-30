from django.core.files.base import ContentFile
from pathlib import Path
from django.core.files import File
from django.core.files.storage import (
    InMemoryStorage,
    Storage,
    FileSystemStorage,
)
from .storages import CustomStorage

from django.shortcuts import render, HttpResponse
from .forms import FileUploadsClassForm
from .models import FileUploadsClass
import os

def index(request):
    if request.method == "POST":
        form = FileUploadsClassForm(request.POST, request.FILES)

        if form.is_valid():
            # instance = form.save(commit=False)
            # instance.save()

            new_file = ContentFile(b"Hello world", name="x.txt")


            # instance = FileUploadsClass(img=request.FILES['img'], file=request.FILES['file'])
            # instance.save()


            # Alternative
            # with open("name.txt", "wb+") as destination:
            #     for chunk in request.FILES['file'].chunks():
            #         destination.write(chunk)
            # handle_uploaded_files(request.FILES['file'])

    else:
        new_file = ContentFile(b"Hello world", name="x.txt")
        # print(new_file.name)
        # print(new_file.size) # bytes

        # with new_file.open("r") as f:
        #     print(f.read())

        # print(new_file.multiple_chunks())

        form = FileUploadsClassForm()

    return render(request, "file_uploads/file_uploads.html", {'form': form})

def index_1(request):
    storage = InMemoryStorage()
    my_file = storage.save("a.txt", ContentFile(b"Hello world"))

    # with storage.open(my_file) as file:
    #     print(file.read().decode('utf-8'))

    # print(storage.exists("a.txt"))
    # print(storage.delete("a.txt"))

    # print(storage.base_url)
    # print(storage.base_location)

    # print(storage.path)
    # print(storage.url)

    # print(dir(storage))


    return HttpResponse("Hello world")

def index_2(request):
    # storage = FileSystemStorage()

    # if not storage.exists("tmp/hello.txt"):
    #     my_file = storage.save("tmp/hello.txt", content=ContentFile(content=b"Hello world from hello.txt"))
    
    # file = storage.open("tmp/hello.txt")
    # print(file.mode)
    # print(file.read) 

    # file.close()

    my_model = FileUploadsClass.objects.first()

    path = Path(f'{os.getcwd()}/media/tmp/hello.txt')

    # print(my_model.img.width)
    # print(my_model.img.height)

    # print(my_model.img.open("r"))

    # with path.open("rb") as f:
    #     my_model.file = File(f, path.name)
    #     my_model.save()
        

    # /home/dexter/dev/django-doc-depth/src/dj/media/tmp/hello.txt




    return HttpResponse("")


def index_3(request):
    my_storage = CustomStorage(location='my_storage', base_url="storageurl")

    my_storage._save("myfile.txt", content=ContentFile(b"Hello world from CustomStorage"))

    # my_storage.delete("20241230_215828_myfile.txt") if my_storage.exists("20241230_215828_myfile.txt") else None 

    # print(my_storage.url("20241230_215834_myfile.txt"))
    return HttpResponse("Hello")