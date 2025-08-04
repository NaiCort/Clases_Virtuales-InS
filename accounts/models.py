from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        SUPERADMIN = "superadmin", "Super-Admin"
        ADMIN      = "admin",      "Administrador"
        TEACHER    = "teacher",    "Docente"
        STUDENT    = "student",    "Estudiante"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    # ------------- helpers ----------------
    @property
    def is_teacher(self) -> bool:
        """Puede impartir cursos si es docente, admin o super-admin."""
        return self.role in {
            self.Role.TEACHER,
            self.Role.ADMIN,
            self.Role.SUPERADMIN,
        }

    @property
    def is_student(self) -> bool:
        return self.role == self.Role.STUDENT

    def __str__(self) -> str:
        return f"{self.username} ({self.get_role_display()})"
