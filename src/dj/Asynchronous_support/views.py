import asgiref.sync
from django.shortcuts import render
from django.http import (
    JsonResponse,
)

# Create your views here.
from asgiref.sync import (
    async_to_sync,
    sync_to_async,
    iscoroutinefunction,
    markcoroutinefunction
)
from .models import (
    Book
)
from django.db import transaction, connection

def books_transaction():
    # Transactions do not yet work in async mode
    with transaction.atomic():
        print("Create a transaction ...")
        book = Book.objects.create(name="Book transaction")
        print("Book created...")


def book_conctions():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Asynchronous_support_book")
        rows = cursor.fetchall()
        return rows

async def index(request):
    # _ = [Book.objects.create(name=f"Book {i}") for i in range(1,7)]
  
    # book = await Book.objects.aget(id=1)

    # book = Book(name="Book 100")
    # await book.asave()

    # book = await Book.objects.acreate(name="Book 1000")

    # book = await sync_to_async(books_transaction)()
    rows = await sync_to_async(book_conctions)()
    print("rows:", rows)



    return JsonResponse({}, safe=False)


@sync_to_async
def index_1(request):

    return JsonResponse({}, safe=False)

# print(iscoroutinefunction(index))
# markcoroutinefunction(index_1)

# print("iscoroutinefunction", iscoroutinefunction(index_1))
