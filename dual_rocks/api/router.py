from rest_framework import routers
from .viewsets import (
    MyProfilesViewSet,
    MyMessagesViewSet
)


router = routers.DefaultRouter()
router.register('my-profiles', MyProfilesViewSet)
router.register('my-messages', MyMessagesViewSet)
