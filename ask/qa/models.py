from django.db import models
from django.contrib.auth.models import User
import datetime


class QuestionManager(models.Manager):
    def new():
        pass
    def popular():
        pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    added_at = models.DateField(default=datetime.date.today())
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')



class Answer(models.Model):
    text = models.TextField(max_length=500)
    added_at = models.DateField(default=datetime.date.today())
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)


