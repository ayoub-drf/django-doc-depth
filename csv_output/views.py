import csv
from django.http import HttpResponse

from .models import Product


def some_view(request):
    # _ = [Product.objects.create(name=f"Product ${i}", price=i, stock_quantity=i) for i in range(1, 11)]
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="products.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(["ID", "name", "price", "quantity"])

    for i in Product.objects.all():
        writer.writerow([i.pk, i.name, i.price, i.stock_quantity])

    return response