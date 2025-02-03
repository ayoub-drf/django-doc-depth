from django.urls import path
from .views import (
    index,
    index_1,
    Index2,
    HomeView
)

urlpatterns = [
    path('', index, name="index"),
    path('index1/', index_1, name="index_1"),
    path('index2/', Index2.as_view(), name="Index2"),
    path('HomeView/', HomeView.as_view(), name="HomeView"),
]