from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100, default='Book')
    content = models.TextField(null=True, blank=True)
    status = models.BooleanField()
    author = models.CharField(max_length=100, null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=100)

                
