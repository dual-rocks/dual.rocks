from django.contrib import admin
from .models import ImageWithPrivacy


@admin.register(ImageWithPrivacy)
class ImageWithPrivacyAdmin(admin.ModelAdmin):
    pass
