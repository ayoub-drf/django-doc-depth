from django.urls import path

from .views import index, index_1, index_3

urlpatterns = [
    path('', index_3)
]
