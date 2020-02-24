from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from dual_rocks.user_profile.models import Profile
from dual_rocks.api.serializers import ProfileSerializer


class MyProfilesViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profiles.all()

    @action(detail=False, url_path='current')
    def current_profile(self, request):
        if request.current_profile:
            serializer = self.get_serializer(request.current_profile)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
