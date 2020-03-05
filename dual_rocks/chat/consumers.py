import uuid
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from dual_rocks.user_profile.middleware import CurrentProfileMiddleware
from dual_rocks.user_profile.models import Profile


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        user = self.scope['user']
        current_profile_id = self.scope['session'].get(
            CurrentProfileMiddleware.CURRENT_PROFILE_ID_FIELD
        )
        self.room_group_name = None
        try:
            self.profile = user.profiles.get(id=current_profile_id)
            self.room_group_name = self.profile.chat_room_group_name
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        except Profile.DoesNotExist:
            self.close()

    async def disconnect(self, close_code):
        if self.room_group_name and self.channel_name:
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self, text_data):
        if text_data == 'PING':
            await self._send_action(
                'PONG',
                {
                    'room_group_name': self.room_group_name,
                    'channel_name': self.channel_name
                }
            )

    async def chat_message(self, event):
        await self._send_action('message', {'message': event.get('message')})

    async def _send_action(self, action, payload):
        await self.send_json({
            'action': action,
            'payload': payload
        })
