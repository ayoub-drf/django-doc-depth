from django.shortcuts import render, HttpResponse
from django.apps import apps
from django.urls import reverse, NoReverseMatch
from .models import Product
from django.core.exceptions import (
    AppRegistryNotReady,
    ObjectDoesNotExist,
    MultipleObjectsReturned,
    EmptyResultSet,
    FieldDoesNotExist,
    SuspiciousOperation,
    PermissionDenied,
    ValidationError,
    MiddlewareNotUsed,
    ImproperlyConfigured,
)

def index(request, val=None):
    # _ = [Product.objects.create(name=f'Product {i}') for i in range(1, 5)]
    
    # -- AppRegistryNotReady
    if not apps.ready:
        raise AppRegistryNotReady("The app registry is not ready yet!")  


    # -- ObjectDoesNotExist & MultipleObjectsReturned
    try:
        # Product.objects.create(name='Product 1')
        # product = Product.objects.get(name='Product 1')
        product = Product.objects.get(pk=1)
    except Product.DoesNotExist:
        raise ObjectDoesNotExist("Product with this ID does not exist.")
    except Product.MultipleObjectsReturned:
        raise MultipleObjectsReturned("Multiple objects returned with this name")
    

    # -- EmptyResultSet
    queryset = Product.objects.filter(name="Product 1")
    if not queryset.exists():
        raise EmptyResultSet("No results found for this query.")
    

    # -- FieldDoesNotExist
    try:
        field = Product._meta.get_field("name")
    except FieldDoesNotExist:
        raise FieldDoesNotExist("The field does not exist in the model.")
    # print(type(field))
    # print(dir(field))

    # -- SuspiciousOperation
    if val:
        if "<script>" in val:
            raise SuspiciousOperation("Possible security risk detected.")

    if request.user.is_authenticated:
        if not request.user.is_staff:
            raise PermissionDenied("")
    
    
    if False:
        raise ValidationError('ValidationError')
    
    try:
        url_p = reverse('index')
    except NoReverseMatch:
        raise NoReverseMatch("URL pattern not found.")

    

    
    return HttpResponse("Hello")
