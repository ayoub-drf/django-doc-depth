from typing import Any
from django.shortcuts import render, HttpResponse, redirect

from django.views.generic import View

from .forms import (
    MyForm,
)

def index(request):
    if request.method == "POST":
        form = MyForm(request.POST)

        if form.is_valid():
            pass

    else:
        form = MyForm()
        rendered_form = form.render('new_forms_1/form_snippet.html')
        

    context = {
        'form': form
    }
    return render(request, "new_forms_1/index.html", context)

