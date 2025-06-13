# courses_backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses_api.views import (
    CourseViewSet,
    CourseInstanceCreateView,
    list_instances_by_year_sem,
    instance_detail,
    course_detail,
)

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/courses/<int:pk>", course_detail),
    path("api/instances", CourseInstanceCreateView.as_view()),
    path("api/instances/<int:year>/<int:semester>", list_instances_by_year_sem),
    path("api/instances/<int:year>/<int:semester>/<int:course_id>", instance_detail),
]
