from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        r"ws/quiz/(?P<room_id>[a-zA-Z0-9_-]+)/(?P<token>[0-9a-f]*)$",
        consumers.QuizConsumer,
    ),
]
