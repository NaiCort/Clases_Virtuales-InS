from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Roles simples usando choices, inspirados en tu tabla anterior
    class Role(models.TextChoices):
        SUPERADMIN = "superadmin", "Super‑Admin"
        ADMIN      = "admin",      "Administrador"
        TEACHER    = "teacher",    "Docente"
        STUDENT    = "student",    "Estudiante"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
