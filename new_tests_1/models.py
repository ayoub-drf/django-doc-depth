from django.db import models
from django.utils.translation import gettext_lazy as _

class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    class Meta:
        verbose_name = _("Animal")
        verbose_name_plural = _("Animals")

    def __str__(self):
        return self.name

    def speak(self):
        return f"The {self.name} says {self.sound}"

