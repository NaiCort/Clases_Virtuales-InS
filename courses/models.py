# courses/models.py
from django.db import models
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    teacher = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.CASCADE,
        related_name="courses",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # ────────── AQUÍ VA EL NUEVO MÉTODO ──────────
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("courses:course_detail", kwargs={"slug": self.slug})
    # ─────────────────────────────────────────────

    def __str__(self):
        return self.title
