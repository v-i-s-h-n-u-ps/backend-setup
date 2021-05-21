from django.contrib import admin

from user.models import *

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Professional)
admin.site.register(Instructor)
admin.site.register(UserSkill)
