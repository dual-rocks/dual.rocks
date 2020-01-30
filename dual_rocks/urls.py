from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .web import urls as web_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(web_urls, namespace='web')),
]

if settings.SERVER_MEDIA_FILES:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
