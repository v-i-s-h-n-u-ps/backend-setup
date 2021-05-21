from django.db import models
from django.db.models import Model


class Role(Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.name


class Technology(Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Schedule(Model):
    type = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Discount(Model):
    name = models.CharField(max_length=50)
    value = models.DecimalField(decimal_places=2, max_digits=7)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class QuestionType(Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class QuestionLevel(Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
