from django.contrib import admin
from django.urls import path, include
from .web import urls as web_urls

urlpatterns = [
    path('', include(web_urls)),
    path('admin/', admin.site.urls),
]
