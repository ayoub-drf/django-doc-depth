from django.http import JsonResponse
from django.db.models import (
    F,
    Value,
    Q,
    When,
    Case,
    Avg,
    Max,
    Min,
    Sum,
    Count,
    Func,
    OuterRef,
    Subquery
)
from django.db.models.functions import (
    Round,
    Length
)
from django.contrib.auth.models import User


from math import ceil

from .models import (
    Product,
)

from django.db.models import QuerySet

def index(req):

    # _ = [Product.objects.create(name=f"Product {i}", price=f"{i}.{i}") for i in range(10)]

    # print( ceil(Product.objects.annotate(new_price=F("price") * 2).last().new_price) )
    # print( Product.objects.filter(Q(name__iexact="product 1") | Q(name__iexact="product 9") ) )

    # filtered_case = Case(
    #     When(pk=1, then=Value("The first one")),
    #     When(pk=10, then=Value("The last one")),
    #     default=Value("Unknown")
    # )
    # print( Product.objects.annotate(extra_value=filtered_case).last().extra_value )

    # calculators = {
    #     "average": Avg("price"),
    #     "sum": Sum("price"),
    #     "max": Max("price"),
    #     "min": Min("price"),
    #     "count": Count("price"),
    # }
    # print( Product.objects.aggregate(**calculators) )

    # print( Product.objects.annotate(name_length=Length("name")).last().name_length )

    # print( Product.objects.annotate(name_upper=Func(F("name"), function="UPPER")).last().name_upper )

    # class Lower(Func):
    #     function = "LOWER"
    # print( Product.objects.annotate(name_lower=Lower("name")).last().name_lower )

    # Most expensive product name for each user
    # users = User.objects.annotate(
    #     most_expensive_product=Subquery(
    #         Product.objects.filter(
    #             customer=OuterRef('pk') # user_pk
    #         ).order_by('-price').values('name')[:1]
    #     )
    # )


    return JsonResponse({}, safe=False)