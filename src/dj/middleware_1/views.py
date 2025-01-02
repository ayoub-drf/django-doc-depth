from django.shortcuts import HttpResponse

from django.db import connection
from asgiref.sync import sync_to_async, iscoroutinefunction

def book_conctions():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Asynchronous_support_book")
        rows = cursor.fetchall()
        return rows

async def index(request):

    rows = await sync_to_async(book_conctions)()
    print("rows:", rows)

    return HttpResponse()

