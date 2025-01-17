from django.db.models.functions import (
    JSONObject,
    MD5,
    SHA1,
    Repeat,
    Replace,
    Extract,
    TruncDay,
    TruncYear,
    Ceil,
    Lower,
    Upper,
    Concat,
    Now,
    ExtractDay,
    ExtractHour,
    ExtractYear,
    ExtractMonth,
    ExtractSecond,
    ExtractWeek,
    Abs,
    Length,
    Cast,
    Coalesce,
    Greatest,
    Least,
    Round,
    Collate,
)

import zoneinfo


from django.db.models import (
    Count,
    Max,
    Min,
    Avg,
    Sum,
    Value,
    CharField,
    IntegerField,
    FloatField,
)

FloatField.register_lookup(Ceil)

from .models import Book

from django.http import JsonResponse

def index(request):
    # _ = [Book.objects.create(name=f"Book {i}") for i in range(2, 11) ]

    # print(Book.objects.annotate(lower_name=Lower('name')).first().lower_name)
    # print(Book.objects.annotate(upper_name=Upper('name')).first().upper_name)
    # print(Book.objects.aggregate(books_count=Count('pk')))
    # print(Book.objects.aggregate(maximum_book=Max('pk')))
    # print(Book.objects.aggregate(minimum_book=Min('pk')))
    # print(Book.objects.aggregate(average_book=Avg('pk')))
    # print(Book.objects.aggregate(books_ids_sum=Sum('pk')))

    # print( Book.objects.annotate(books_pk_name=Concat('pk', 'name', output_field=CharField())).first().books_pk_name )
    
    # print( Book.objects.annotate(current_time=Now()).first().current_time )

    # print( Book.objects.annotate(current_year=ExtractYear('created')).first().current_year )
    # print( Book.objects.annotate(current_day=ExtractDay('created')).first().current_day )

    # print( Book.objects.annotate(price_abs=Abs('price')).first().price_abs )

    # print( Book.objects.annotate(name_length=Length('name')).first().name_length )

    # print( Book.objects.annotate(pk_as_float=Cast('pk', output_field=FloatField())).first().pk_as_float )

 
    # print( Book.objects.annotate(status_default_unknown=Coalesce('status', Value('Unknown'), output_field=CharField() )).last().status_default_unknown )

    # print( Book.objects.annotate(greatest_value=Greatest('pk', 'price', output_field=FloatField() )).last().greatest_value )
    # print( Book.objects.annotate(least_value=Least('pk', 'price', output_field=FloatField() )).last().least_value )

    # book = Book.objects.latest('created')
    # book.price = 2.2992
    # book.save()

    # print( Book.objects.annotate(price_round=Round('price')).latest('created').price_round )

    # print( Book.objects.annotate(json_obj=JSONObject(name="name", pk='pk')).first().json_obj )

    # print( Book.objects.annotate(get_year=Extract('created', 'year')).first().get_year )

    # print( Book.objects.annotate(get_year=TruncYear('created')).first().get_year )

    # print( Book.objects.annotate(apply_ceil=Ceil('price')).first().apply_ceil )

    # print( Book.objects.annotate(name_hash=MD5('name')).first().name_hash ) # Hash the

    # print( Book.objects.annotate(name_rep=Repeat('name', 10)).first().name_rep )

    return JsonResponse({"msg": "ok"}, safe=False)
