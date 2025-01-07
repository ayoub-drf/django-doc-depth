from django.shortcuts import render

from .models import Book
from django.http import JsonResponse

def index(request):
    # _ = [Book.objects.create(name=f"Book {i}") for i in range(1, 3)]

    # print(Book.objects.filter(name__custom_like="Book 2"))
    print(Book.objects.filter(name__not_equal="Book 2"))
    

    return JsonResponse({"msg": "ok"}, safe=False)
