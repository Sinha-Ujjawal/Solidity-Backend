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
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    room_id = models.CharField(max_length=16, unique=True)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="questions"
    )
    question = models.TextField(max_length=500)


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options"
    )
    option = models.CharField(max_length=200)
    is_answer = models.BooleanField(default=False)
