from django.db.models import Model
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from masterdata.models import Role, Technology
from user.managers import CustomUserManager


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(max_length=13)
    github_url = models.CharField(max_length=200, blank=True)
    fcm_token = models.CharField(max_length=128, null=True, blank=True, help_text='firebase cloud token')
    login_type = models.CharField(max_length=20, help_text='EMAIL, GOOGLE, FB', default='EMAIL')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    last_login = models.DateTimeField(auto_now=True)
    registered_on = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name + ": " + self.email


class Student(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=200, blank=True)
    year_enrolled = models.IntegerField(default=0)
    course_duration = models.IntegerField(default=0)
    course_type = models.CharField(max_length=50, help_text='BTech, BSc, BA ....', blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.email + ": " + self.college


class Professional(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200, blank=True)
    experience = models.IntegerField(default=0)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.email + ": " + self.company


class Instructor(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=200, blank=True)
    training_experience = models.IntegerField(default=0)
    work_experience = models.IntegerField(default=0)
    city = models.CharField(max_length=100, blank=True)
    salary = models.DecimalField(decimal_places=2, max_digits=11)

    def __str__(self):
        return self.user.email + ": " + self.salary


class UserSkill(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ": " + self.technology.name
