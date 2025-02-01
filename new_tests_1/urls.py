from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('form_submitted/', form_submitted, name="form_submitted"),
    path('index2/', index_2, name="index2"),
]
