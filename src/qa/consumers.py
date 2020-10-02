from asyncio import events
from channels.generic.websocket import JsonWebsocketConsumer
from asgiref.sync import async_to_sync
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, AnonymousUser
from .models import Quiz


class QuizConsumer(JsonWebsocketConsumer):
    def __init__(self) -> None:
        try:
            token = self.scope["url_quote"]["kwargs"]["token"]
            room_id = self.scope["url_quote"]["kwargs"]["token"]

            self.user: User = self.get_user(token=token)

            d = Quiz.objects.get(room_id=room_id)
            self.room_id = d.room_id
            self.host_id = d.user_id
            self.room_id = room_id

            # Join room group
            async_to_sync(self.channel_layer.group_add)(self.room_id, self.channel_name)

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_id,
                {"type": "chat_hola"},
            )

            self.accept()
        except Quiz.DoesNotExist:
            self.close()

    @staticmethod
    def get_user(token) -> User:
        try:
            return Token.objects.get(key=token).user
        except Token.DoesNotExist:
            return AnonymousUser()

    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.room_id, self.channel_name)
        if self.user.is_anonymous:
            self.user.delete()

    def chat_hola(self, event):
        self.send_json(
            {
                "user": self.user.id,
                "message": "hola",
                "is_anonymous": self.user.is_anonymous,
            }
        )
