from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Lesson

def lesson_page(request, id):
    lesson = get_object_or_404(Lesson, id=id)

    return render(request, "lessons/lesson_page.html", {
        "lesson": lesson
    })


from django.shortcuts import render, redirect, get_object_or_404
from .models import Lesson
from courses.models import Course


# Lesson Page
def lesson_page(request, id):
    lesson = get_object_or_404(Lesson, id=id)

    return render(request, "lessons/lesson_page.html", {
        "lesson": lesson
    })


# Dashboard Lesson List
def lesson_dashboard(request):
    lessons = Lesson.objects.all()

    return render(request, "lessons/lesson_dashboard.html", {
        "lessons": lessons
    })


# Add Lesson
def add_lesson(request):

    courses = Course.objects.all()

    if request.method == "POST":

        title = request.POST['title']
        content = request.POST['content']
        video_url = request.POST['video_url']
        course_id = request.POST['course']

        course = Course.objects.get(id=course_id)

        Lesson.objects.create(
            title=title,
            content=content,
            video_url=video_url,
            course=course
        )

        return redirect("lesson_dashboard")

    return render(request, "lessons/add_lesson.html", {
        "courses": courses
    })

# Edit Lesson
def edit_lesson(request, id):

    lesson = get_object_or_404(Lesson, id=id)
    courses = Course.objects.all()

    if request.method == "POST":

        lesson.title = request.POST['title']
        lesson.content = request.POST['content']
        lesson.video_url = request.POST['video_url']
        lesson.course_id = request.POST['course']

        lesson.save()

        return redirect("lesson_dashboard")

    return render(request, "lessons/edit_lesson.html", {
        "lesson": lesson,
        "courses": courses
    })

# Delete Lesson
def delete_lesson(request, id):

    lesson = get_object_or_404(Lesson, id=id)
    lesson.delete()

    return redirect("lesson_dashboard")    