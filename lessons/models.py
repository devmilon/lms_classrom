from django.db import models

# Create your models here.
from django.db import models
from courses.models import Course

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.title