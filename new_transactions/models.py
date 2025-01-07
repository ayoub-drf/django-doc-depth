from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(max_length=32, default="Product")
    stock = models.IntegerField(default=20)

class Order(models.Model):
    product = models.ForeignKey("Product", verbose_name=_("Product"), on_delete=models.CASCADE)
    quantity = models.IntegerField()
