from django.http import HttpResponse
from decimal import Decimal
from datetime import date
from django.db.models import (
    Avg,
    Max,
    Min,
    Count,
    Q
)

from .models import (
    Author,
    Publisher,
    Book,
)

def index(request):
    # _ = [Author.objects.create(name=f"Author {i}") for i in range(3)]
    # _ = [Publisher.objects.create(name=f"Publisher {i}") for i in range(3)]

    # book = [Book.objects.create(price=Decimal(f"{i}.9{i}"), rating=f"{i}.5", publisher=Publisher.objects.first(), pubdate=date(2023, 5, 12)) for i in range(2)]
    # _ = Book.objects.last().authors.add(Author.objects.first(), Author.objects.last())
    # book = Book.objects.last()
    # book.publisher = Publisher.objects.get(id=2)
    # book.save()

    # print(Book.objects.count())
    # print(Book.objects.filter(publisher__name__iexact="publisher 1").first().publisher.name)
    # print(Book.objects.aggregate(average_price=Avg("price", default=0)))
    # print(Book.objects.aggregate(min_price=Min("price", default=0)))
    # print(Book.objects.aggregate(max_price=Max("price", default=0)))
    # print(Book.objects.aggregate(total_price=Count("price")))

    # Add extra attr to Publisher
    # print(Publisher.objects.annotate(total_books=Count("book")).last().total_books)

    # book = Book.objects.first()

    # book_id_equal_1 = Count("book", filter=Q(book__pk=1))
    # print(Publisher.objects.annotate(book_id_equal_1=book_id_equal_1).last().book_id_equal_1)
    print(Book.objects.annotate(authors_count=Count("authors")).last().authors_count)


    return HttpResponse("Hello world")