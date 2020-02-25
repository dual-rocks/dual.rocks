from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from dual_rocks.chat.models import Message
from dual_rocks.api.serializers import MessageSerializer


class MyMessagesViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.current_profile:
            return None
        return self.request.current_profile.messages

    def perform_create(self, serializer):
        serializer.save(from_profile=self.request.current_profile)
