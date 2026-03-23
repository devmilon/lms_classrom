from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.shortcuts import render
from lessons.models import Lesson
from .models import Course

def home(request):
    courses = Course.objects.all()[:6]
    return render(request, "home.html", {"courses": courses})

def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses": courses})

@login_required
def course_create(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        price = request.POST.get("price")

        Course.objects.create(
            instructor=request.user,
            title=title,
            description=description,
            price=price
        )

        return redirect("course_list")  # dashboard or list page

    return render(request, "courses/course_create.html")

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    lessons = Lesson.objects.filter(course=course)

    context = {
        "course": course,
        "lessons": lessons
    }

    return render(request, "courses/course_detail.html", context)