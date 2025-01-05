from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404,
    HttpResponse,
)

from django.template import loader

from .models import (
    Product
)

def index(request):
    # _ = [Product.objects.create(name=f"Product {i}") for i in range(6)]

    print(get_object_or_404(Product, pk=1).name)
    print(get_list_or_404(Product, pk=1)[0].pk)
    print(get_list_or_404(Product))

    tem = loader.get_template('404.html')

    return HttpResponse(tem.render({'name': "dexter"}, request))