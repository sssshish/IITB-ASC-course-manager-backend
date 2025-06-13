#serializers.py
from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseInstanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), write_only=True, source='course'
    )

    class Meta:
        model = CourseInstance
        fields = ['id', 'course', 'course_id', 'year', 'semester']
