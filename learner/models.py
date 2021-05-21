from django.db import models
from django.db.models import Model

from masterdata.models import Technology, Discount, Schedule, QuestionLevel, QuestionType
from user.models import Instructor, User


class Course(Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    technology = models.ForeignKey(Technology, on_delete=models.DO_NOTHING)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    payment_link = models.CharField(max_length=200, blank=True)
    duration = models.IntegerField(default=0, help_text='# of hours for the course')
    session_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Session(Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    payment_link = models.CharField(max_length=200, blank=True)
    duration = models.IntegerField(default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    session_url = models.CharField(max_length=200, blank=True)
    recording_url = models.CharField(max_length=200, blank=True)
    lecture_slides = models.CharField(max_length=200, blank=True)
    lecture_notes = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Notes(Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    firebase_url = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session.name + ": " + self.firebase_url


class SessionAttendance(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    login_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session.name + ": " + self.user.name + "= " + self.login_time


class MultipleAnswerQuestion(Model):
    question = models.CharField(max_length=500)
    choices = models.CharField(max_length=250, help_text='[option 1, option 2, option 3, option 4]')
    answers = models.CharField(max_length=20, help_text='[0,3]: indices of the options array with correct options')

    def __str__(self):
        return self.question


class SingleAnswerQuestion(Model):
    question = models.CharField(max_length=500)
    choices = models.CharField(max_length=250, help_text='[option 1, option 2, option 3, option 4]')
    answer = models.CharField(max_length=2, help_text='1: index of the options array with correct options')

    def __str__(self):
        return self.question


class SessionAssignment(Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    level = models.ForeignKey(QuestionLevel, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(QuestionType, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(MultipleAnswerQuestion, on_delete=models.CASCADE)
    point = models.IntegerField(default=1)

    def __str__(self):
        return self.session.id + ": " + self.level.name + ", " + self.type.name


class SessionAssignmentResult(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_assignment = models.ForeignKey(SessionAssignment, on_delete=models.CASCADE)
    point = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_assignment.id + ": " + self.user.name


class Certificate(Model):
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    details = models.CharField(max_length=400, blank=True)
    certificate_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name + ": " + self.certificate_id


class CourseEnrollment(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    certificate = models.ForeignKey(Certificate, on_delete=models.DO_NOTHING)
    status = models.IntegerField(help_text='completed, on going, incompleted')
    points_earned = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ": " + self.certificate.certificate_id


class Payment(Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    discount = models.ForeignKey(Discount, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    transaction_id = models.CharField(max_length=50)
    gateway_id = models.CharField(max_length=100, help_text='payment gateway id')
    status = models.CharField(max_length=10, help_text='success, failed')
    purchased_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ": " + self.course.name