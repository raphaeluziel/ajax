from django.conf import settings
from django.db import models


class Player(models.Model):
    player = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    questions_answered = models.ManyToManyField('Question', blank=True)
    score = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.player.first_name + " " + self.player.last_name


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category


class Question(models.Model):
    question = models.CharField(max_length=200)
    value = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    correct_answer = models.OneToOneField('Answer', on_delete=models.CASCADE, related_name='correct_answer', null=True)

    def __str__(self):
        return self.category.category + ": " + self.question


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')

    def __str__(self):
        return self.question.question + ": " + self.answer
