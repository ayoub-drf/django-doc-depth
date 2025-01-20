from django.shortcuts import render
from .forms import (
    MyForm,
)
from django.core.files.base import ContentFile
from django.db.models import FileField
from django.core.files.uploadedfile import UploadedFile

from django.core.validators import validate_email



def index(request):
    data = {
        'recipients': 'x@aol.com',
        'phone_number': "1425789654",
        'num': 32,
        'username': "james",
        'name': "james",
        'password': "confirm_pasfsword",
        'confirm_password': "confirm_password",
    }
    form = MyForm(data=data)
    print('form.is_valid(): ', form.is_valid())

    if form.is_valid():
        pass
    

    # # print(form.errors)
    print(form.non_field_errors())
    context = {
        'form': form
    }
    return render(request, 'new_form_validation/index.html', context)
