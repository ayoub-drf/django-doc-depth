from django.db import models
from django.contrib import admin
from django.utils.html import format_html

class Author(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publisher = models.ManyToManyField(Publisher, related_name='books')
    published_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.title
    
    @admin.display
    def colored_title(self):
        return format_html(
            '<span style="color: #{}; font-weight: {};">{}</span>',
            '2196D3',
            'bold',
            self.title,
        )
    
    @admin.display(boolean=True)
    def born_in_fifties(self):
        return 1950 <= 1999 >= 1960
