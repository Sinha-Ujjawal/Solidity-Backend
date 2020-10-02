from typing import List, Dict
import secrets
from django.contrib.auth.models import User
from .models import *


def create_quiz(*, user: User, quiz_questions: List[Dict[str, str]]):
    quiz = Quiz.objects.create(user_id=user, room_id=secrets.token_urlsafe(10))

    questions = Question.objects.bulk_create(
        [
            Question(quiz_id=quiz, question=quiz_question["question"])
            for quiz_question in quiz_questions
        ]
    )

    Option.objects.bulk_create(
        [
            Option(
                question_id=question,
                option=choice,
                is_answer=choice == quiz_question["answer"],
            )
            for quiz_question, question in zip(quiz_questions, questions)
            for choice in quiz_question["choices"]
        ]
    )

    return quiz.room_id
