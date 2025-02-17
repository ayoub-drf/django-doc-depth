from django.urls import path
from .views import *

from .admin import admin_site

urlpatterns = [
    path("myadmin/", admin_site.urls),
    path('', index)
]
