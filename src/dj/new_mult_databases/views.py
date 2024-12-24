from django.http import HttpResponse
from django.db import transaction

from .models import Book

def index(request):
    # _ = [Book.objects.using('secondary').create(name=f'Book {i}') for i in range(5, 10)]

    with transaction.atomic(using="secondary"):
        _ = Book.objects.first().delete()

        print("book deleted")

    print(Book.objects.using("secondary").all())

    return HttpResponse(".")

