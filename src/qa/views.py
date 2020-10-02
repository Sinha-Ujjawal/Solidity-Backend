from django.http import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import serializers
from rest_framework.views import APIView
from .services import *


class QuizQuestionsSerializers(serializers.Serializer):
    question = serializers.CharField(max_length=500)
    choices = serializers.ListField()
    answer = serializers.CharField(max_length=200)


class QuizSerializers(serializers.Serializer):
    quizQuestions = serializers.ListField(child=QuizQuestionsSerializers())


class Quiz(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = QuizSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "room_id": create_quiz(
                    user=request.user,
                    quiz_questions=serializer.validated_data["quizQuestions"],
                )
            }
        )
