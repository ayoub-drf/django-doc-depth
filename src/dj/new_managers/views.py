from django.http import HttpResponse
from .models import Book

from django.db.models import Value
from django.db.models.functions import Coalesce

def index(request):
    first_book = Book.objects.annotate(default_name=Coalesce("name", Value("Unknown"))).first()
    # print(first_book.default_name)

    print(Book.manager_one.all())

    return HttpResponse("Hello world")
