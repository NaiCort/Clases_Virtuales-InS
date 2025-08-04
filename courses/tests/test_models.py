import pytest
from courses.models import Course, Lesson, Enrollment
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_course():
    teacher = User.objects.create_user(username="docente", password="pass", autorizacion="administrador")
    course = Course.objects.create(title="Matemáticas I", description="Intro", teacher=teacher)
    assert course.slug == "matematicas-i"
