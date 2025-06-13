#views.py
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['GET', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    if request.method == 'DELETE':
        course.delete()
        return Response(status=204)


class CourseInstanceCreateView(generics.CreateAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer


@api_view(['GET'])
def list_instances_by_year_sem(request, year, semester):
    instances = CourseInstance.objects.filter(year=year, semester=semester)
    serializer = CourseInstanceSerializer(instances, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def instance_detail(request, year, semester, course_id):
    try:
        instance = CourseInstance.objects.get(year=year, semester=semester, course__id=course_id)
    except CourseInstance.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CourseInstanceSerializer(instance)
        return Response(serializer.data)

    if request.method == 'DELETE':
        instance.delete()
        return Response(status=204)
