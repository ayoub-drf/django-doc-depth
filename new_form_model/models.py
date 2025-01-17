from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Author(models.Model):
    name = models.CharField(max_length=100)   

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class Book(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    authors = models.ManyToManyField("Author")

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})

