from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import MyForm
from asgiref.sync import sync_to_async
from .models import Animal
import json

@sync_to_async
def get_animals():

    return list(Animal.objects.all())

async def index_2(request):
    # animals = await sync_to_async(get_animals)()
    animals = await get_animals()

    return JsonResponse({"name": "animal"}, safe=False)


def index_1(request):
    return JsonResponse({"message": "Hello world"}, safe=False)

def form_submitted(request):
    return HttpResponse("Form submitted")

@login_required
def home(request):
    _  = [Animal.objects.create(name=i.get('name'), sound=i.get('sound')) for i in [{'name': "cat", 'sound': "meow"}, {'name': "dog", 'sound': "bark"}]]
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is Valid")
            return redirect("form_submitted")
        else:
            print("Form is not Valid")
    else:
        form = MyForm()

    context = {
        "form": form
    }

    return render(request, "new_tests_1/index.html", context)