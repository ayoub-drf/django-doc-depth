from django.contrib import admin
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # /home/dexter/dev/django-doc-depth/src/dj/static/css/styles.css
    
    # path('urls/', include('new_URLconfs.urls', namespace="new_URLconfs")),
    path('', include('req_res_obj.urls')),

] + debug_toolbar_urls()

# Serving files in development
if settings.DEBUG:
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]

