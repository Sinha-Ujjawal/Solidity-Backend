from typing import List, Dict
import secrets
from django.contrib.auth.models import User
from .models import *


def create_quiz(*, user: User, quiz_questions: List[Dict[str, str]]):
    quiz = Quiz(user_id=user, room_id=secrets.token_bytes(16))

    questions = []
    options = []
    for quiz_question in quiz_questions:
        question = Question(quiz_id=quiz.id, question=quiz_question["question"])
        answer = quiz_question["answer"]
        choices = quiz_question["choices"]
        assert answer in choices
        for choice in choices:
            option = Option(
                question_id=question.id, option=choice, is_answer=choice == answer
            )
            options.append(option)
        questions.append(question)

    Question.objects.bulk_create(questions)
    Option.objects.bulk_create(options)

    quiz.save()
    return quiz.room_id
