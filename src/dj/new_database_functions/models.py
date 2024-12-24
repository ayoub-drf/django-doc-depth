from django.db import models
from django.utils.timezone import now

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=3, default=2.2)
    status = models.BooleanField(null=True)
    created = models.DateTimeField(default=now)

    def __str__(self):
        return "%s" % self.name
    
