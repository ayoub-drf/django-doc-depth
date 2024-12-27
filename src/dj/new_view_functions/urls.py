from django.urls import (
    path,
    re_path, # (?P<name>[A-z]+)/$
)
from . import views



urlpatterns = [
    path('', views.get_posts),
]
