from typing import List, Dict
import secrets
from django.contrib.auth.models import User
from .models import *


def create_quiz(*, user: User, quiz_questions: List[Dict[str, str]]):
    quiz = Quiz.objects.create(user_id=user, room_id=secrets.token_urlsafe(10))

    for quiz_question in quiz_questions:
        question = Question.objects.create(
            quiz_id=quiz.id, question=quiz_question["question"]
        )

        answer = quiz_question["answer"]
        choices = quiz_question["choices"]

        assert answer in choices

        Option.objects.bulk_create(
            [
                Option(
                    question_id=question.id, option=choice, is_answer=choice == answer
                )
                for choice in choices
            ]
        )

    return quiz.room_id
