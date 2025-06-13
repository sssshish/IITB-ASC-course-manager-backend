#models.py
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.code} - {self.title}"


class CourseInstance(models.Model):
    course = models.ForeignKey(Course, related_name='instances', on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    semester = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('course', 'year', 'semester')

    def __str__(self):
        return f"{self.course.code} - {self.year}-S{self.semester}"
