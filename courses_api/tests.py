from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Course, CourseInstance

class CourseAPITests(APITestCase):
    def setUp(self):
        self.course_data = {
            'title': 'Intro to Python',
            'code': 'CS101',
            'description': 'Learn Python from scratch'
        }
        self.course = Course.objects.create(**self.course_data)

    def test_create_course(self):
        data = {
            'title': 'Data Structures',
            'code': 'CS102',
            'description': 'Basics of data structures'
        }
        response = self.client.post('/api/courses/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)

    def test_get_courses(self):
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_course_detail(self):
        response = self.client.get(f'/api/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['code'], 'CS101')

    def test_delete_course(self):
        response = self.client.delete(f'/api/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)

class CourseInstanceAPITests(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Algorithms',
            code='CS103',
            description='Intro to algorithms'
        )
        self.instance = CourseInstance.objects.create(
            course=self.course,
            year=2023,
            semester=1
        )

    def test_create_course_instance(self):
        data = {
            'course_id': self.course.id,
            'year': 2024,
            'semester': 2
        }
        response = self.client.post('/api/instances/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CourseInstance.objects.count(), 2)

    def test_list_instances_by_year_sem(self):
        response = self.client.get('/api/instances/2023/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_instance_detail(self):
        response = self.client.get(f'/api/instances/2023/1/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['year'], 2023)

    def test_delete_instance(self):
        response = self.client.delete(f'/api/instances/2023/1/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CourseInstance.objects.count(), 0)
