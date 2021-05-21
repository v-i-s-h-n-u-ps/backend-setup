
from django.urls import path

from masterdata.views import *

urlpatterns = [
    path('list_roles/', ListRoles.as_view(), name='list_roles'),
]
