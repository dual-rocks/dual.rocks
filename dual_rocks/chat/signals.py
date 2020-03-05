from asgiref.sync import async_to_sync
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from dual_rocks.api.serializers import MessageSerializer
from .models import Message


channel_layer = get_channel_layer()


@receiver(post_save, sender=Message)
def post_save_message(sender, instance, created, **kwargs):
    if created:
        message_data = MessageSerializer(instance).data
        async_to_sync(channel_layer.group_send)(
            instance.from_profile.chat_room_group_name,
            {'type': 'chat.message', 'message': message_data},
        )
        async_to_sync(channel_layer.group_send)(
            instance.to_profile.chat_room_group_name,
            {'type': 'chat.message', 'message': message_data},
        )
