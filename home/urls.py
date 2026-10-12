from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="index"),
    path("employee/<int:employee_id>/",views.employee_details,name="employee_details"),
]