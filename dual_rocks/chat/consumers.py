import uuid
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from dual_rocks.user_profile.models import Profile


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        current_profile_id = self.scope['session'].get('current_profile_id')
        try:
            self.profile = user.profiles.get(id=current_profile_id)
            self.room_group_name = self.profile.chat_room_group_name
            self.channel_name = str(uuid.uuid4())
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()
        except Profile.DoesNotExist:
            self.close()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        if text_data == 'PING':
            self._send_action(
                'PONG',
                {
                    'room_group_name': self.room_group_name,
                    'channel_name': self.channel_name
                }
            )
            return

    def _send_action(self, action, payload):
        self.send(text_data=json.dumps({
            'action': action,
            'payload': payload
        }))
