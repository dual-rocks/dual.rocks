from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django_filters import rest_framework as filters
from dual_rocks.chat.models import Message
from dual_rocks.api.serializers import MessageSerializer
from dual_rocks.api.filters import MessageFilter


class MyMessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        if not self.request.current_profile:
            raise NotFound
        return self.request.current_profile.messages

    def perform_create(self, serializer):
        serializer.save(from_profile=self.request.current_profile)
