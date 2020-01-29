from django.contrib import admin
from django.urls import path, include
from .web import urls as web_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(web_urls, namespace='web')),
]
