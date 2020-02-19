from django.contrib import admin
from .models import (
    Profile,
    Photo,
    UserViewPhoto,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(UserViewPhoto)
class UserViewPhotoAdmin(admin.ModelAdmin):
    pass
