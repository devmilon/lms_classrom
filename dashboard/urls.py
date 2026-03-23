from django.urls import path
from .views import student_dashboard, instructor_dashboard

urlpatterns = [

    path("student/", student_dashboard, name="student_dashboard"),

    path("instructor/", instructor_dashboard, name="instructor_dashboard"),

]