from rest_framework import routers
from .viewsets import MyProfilesViewSet


router = routers.DefaultRouter()
router.register('my-profiles', MyProfilesViewSet)
