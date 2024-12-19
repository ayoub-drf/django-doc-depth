from django.http import HttpResponse
from .models import (
    Product,
    Order,
)
from django.db import transaction


def index(request):
    # _ = [Product.objects.create() for i in range(10)]
    product = Product.objects.first()
    quantity = 30
    res = "OK"

    with transaction.atomic():
        if product.stock < quantity:
            return HttpResponse(f"NOT ENOUGH STOCK: ({product.stock}) FOR THE QUANTITY: ({quantity})")
        
        product.stock -= quantity
        product.save()

        order = Order.objects.create(product=product, quantity=quantity)

        print(f"transaction succeed => ORDER ID: {order.id}")

    res += f" Order Count: {Order.objects.count()} Product  Stock: {product.stock}"
    


    return HttpResponse(res)

def index_1(request):
    quantity = 13
    res = "OK"

    transaction.set_autocommit(False)

    try:
        # select_for_update: lock the product rows until the transaction is done
        product = Product.objects.select_for_update().last()
        if product.stock < quantity:
            raise ValueError(f"NOT ENOUGH STOCK: ({product.stock}) FOR THE QUANTITY: ({quantity})")
        
        product.stock -= quantity
        product.save()

        order = Order.objects.create(product=product, quantity=quantity)

        print(f"transaction succeed => ORDER ID: {order.id}")
        transaction.commit()
    except Exception as e:
        transaction.rollback()
        return HttpResponse(f"{e}")
    finally:
        transaction.set_autocommit(True)

    res += f" Order Count: {Order.objects.count()} Product  Stock: {product.stock}"
    


    return HttpResponse(res)
