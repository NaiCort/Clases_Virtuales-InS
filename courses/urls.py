from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course_list"),
    path("<slug:slug>/", views.CourseDetailView.as_view(), name="course_detail"),
    path("my/", views.MyCoursesView.as_view(), name="my_courses"),
]

# rutas para docentes
from .views_teacher import (
    MyTeacherCoursesView,
    CourseCreateView, CourseUpdateView, CourseDeleteView,
    LessonCreateView, LessonUpdateView, LessonDeleteView,
)

urlpatterns += [
    path("teacher/", MyTeacherCoursesView.as_view(), name="teacher_course_list"),
    path("teacher/create/", CourseCreateView.as_view(), name="course_create"),
    path("teacher/<slug:slug>/edit/", CourseUpdateView.as_view(), name="course_edit"),
    path("teacher/<slug:slug>/delete/", CourseDeleteView.as_view(), name="course_delete"),

    path("teacher/<slug:slug>/lessons/add/", LessonCreateView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/edit/", LessonUpdateView.as_view(), name="lesson_edit"),
    path("lessons/<int:pk>/delete/", LessonDeleteView.as_view(), name="lesson_delete"),
]
