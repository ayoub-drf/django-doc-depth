from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('urls/', include('new_URLconfs.urls', namespace="new_URLconfs")),
    path('', include('new_view_functions.urls')),

] + debug_toolbar_urls()


