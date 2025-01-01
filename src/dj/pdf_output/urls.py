from django.urls import path

from .views import (
    generate_pdf,
)

urlpatterns = [
    path("", generate_pdf)
]
