from django.contrib import admin

from masterdata.models import *

admin.site.register(Role)
admin.site.register(Technology)
admin.site.register(Schedule)
admin.site.register(QuestionLevel)
admin.site.register(QuestionType)
admin.site.register(Discount)