from datetime import date

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, default="Author")
    def __str__(self):
        return f'{self.pk}'

class Blog(models.Model):
    name = models.CharField(max_length=100, default="blog")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="blogs", null=True)

    def __str__(self):
        return f'{self.pk}'


