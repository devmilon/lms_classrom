# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):

    return render(request,
                  "dashboard/student_dashboard.html")

from django.contrib.auth.decorators import login_required

@login_required
def instructor_dashboard(request):

    return render(request,
                  "dashboard/instructor_dashboard.html")