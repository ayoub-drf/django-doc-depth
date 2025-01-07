from . import views
from django.urls import path

urlpatterns = [
    path('one/', views.index)
]
