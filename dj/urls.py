from django.contrib import admin
from django.urls import path, include, re_path
from debug_toolbar.toolbar import debug_toolbar_urls

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # /home/dexter/dev/django-doc-depth/src/dj/static/css/styles.css
    
    # path('urls/', include('new_URLconfs.urls', namespace="new_URLconfs")),
    path('', include('new_internationalization.urls')),

] 



# Serving files in development
if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ] 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

