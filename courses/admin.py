from django.contrib import admin
from .models import Course, Lesson, Enrollment

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "teacher", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [LessonInline]

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "status", "progress", "enrolled_at")
    list_filter = ("status", "course")
