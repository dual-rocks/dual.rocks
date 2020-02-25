from rest_framework import serializers
from dual_rocks.chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'from_profile',
            'to_profile',
            'content',
            'created_at'
        ]
        read_only_fields = [
            'from_profile'
        ]
