from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    added_at = models.DateField()
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.IntegerField(default=0)


class Answer(models.Model):
    text = models.CharField(max_length=500)
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

