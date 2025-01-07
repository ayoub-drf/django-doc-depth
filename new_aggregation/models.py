from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    def __str__(self):
        return f"{self.pk}"
    
