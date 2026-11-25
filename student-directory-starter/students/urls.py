from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_list, name="student-list"),
    path("students/<int:student_id>/", views.student_detail, name="student-detail"),
    path("health/", views.health, name="health"),
]