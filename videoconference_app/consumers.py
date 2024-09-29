# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class WebinarConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.meeting_id = self.scope['url_route']['kwargs']['meeting_id']
        self.peer_id = self.channel_name  # Har bir foydalanuvchi uchun noyob identifikator
        self.meeting_group_name = f'webinar_{self.meeting_id}'

        # WebSocketga ulanish
        await self.channel_layer.group_add(
            self.meeting_group_name,
            self.channel_name
        )
        await self.accept()

        # Foydalanuvchiga yangi peerId jo'natish
        await self.send(json.dumps({'peerId': self.peer_id}))

    async def disconnect(self, close_code):
        # WebSocketdan ajralish
        await self.channel_layer.group_discard(
            self.meeting_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        message_data = json.loads(text_data)
        peer_id = message_data.get('peerId', self.peer_id)  # Kimdan xabar keldi

        # Signaling messagesni hamma foydalanuvchilarga yuborish
        await self.channel_layer.group_send(
            self.meeting_group_name,
            {
                'type': 'webinar_message',
                'message': message_data,
                'peer_id': peer_id
            }
        )

    async def webinar_message(self, event):
        message = event['message']
        peer_id = event['peer_id']

        # PeerIdni boshqa foydalanuvchilarga yuborish
        message['peerId'] = peer_id

        # Xabarni WebSocket orqali yuborish
        await self.send(text_data=json.dumps(message))
