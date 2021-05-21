from django.contrib import admin

from learner.models import *

admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Notes)
admin.site.register(SessionAttendance)
admin.site.register(MultipleAnswerQuestion)
admin.site.register(SingleAnswerQuestion)
admin.site.register(SessionAssignment)
admin.site.register(SessionAssignmentResult)
admin.site.register(Certificate)
admin.site.register(CourseEnrollment)
admin.site.register(Payment)
