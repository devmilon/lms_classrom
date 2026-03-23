
from django.urls import path
from . import views

urlpatterns = [

    path('<int:id>/', views.lesson_page, name='lesson_page'),

    path('lesson-dashboard/', views.lesson_dashboard, name='lesson_dashboard'),

    path('add-lesson/', views.add_lesson, name='add_lesson'),

    path('edit-lesson/<int:id>/', views.edit_lesson, name='edit_lesson'),

    path('delete-lesson/<int:id>/', views.delete_lesson, name='delete_lesson'),

]