from django.conf import settings
from django.db import models
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

class Course(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=180)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)
    video_url = models.URLField(blank=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.title}"


class Enrollment(models.Model):
    ACTIVE = "activo"
    COMPLETED = "completado"

    STATUS_CHOICES = [
        (ACTIVE, "Activo"),
        (COMPLETED, "Completado"),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=ACTIVE)
    progress = models.PositiveIntegerField(default=0)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student} ↔︎ {self.course}"
