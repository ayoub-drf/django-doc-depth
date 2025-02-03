from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    name = models.CharField(_("name"), max_length=50)    

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.name


