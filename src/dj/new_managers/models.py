from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

class BookManagerOne(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(author="james") & Q(name__isnull=True))

class Book(models.Model):
    TYPE_CHOICES = (
        ("C", _("Comedy")),
        ("F", _("Fantasy"))
    )
    name = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, default="james")
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default="C")

    objects = models.Manager()

    manager_one = BookManagerOne()

    def __str__(self):
        return f"{self.name} : {self.author} : {self.get_type_display()}"
    

    