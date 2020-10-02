#!/usr/bin/env python
"""
    @author : Ujjawal Sinha
    @email : ujjawalsinhacool16021998@gmail.com
    @created at : 2020-09-26 22:26:35
    @desc : Database Models for Quiz
"""
from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    id = models.IntegerField(primary_key=True)
    room_id = models.CharField(max_length=16, unique=True)


class Question(models.Model):
    quiz_id = models.OneToOneField(
        Quiz, on_delete=models.CASCADE, related_name="questions"
    )
    id = models.IntegerField(primary_key=True)
    question = models.TextField(max_length=500)


class Option(models.Model):
    question_id = models.OneToOneField(
        Question, on_delete=models.CASCADE, related_name="options"
    )
    id = models.IntegerField(primary_key=True)
    option = models.CharField(max_length=200)
    is_answer = models.BooleanField(default=False)
