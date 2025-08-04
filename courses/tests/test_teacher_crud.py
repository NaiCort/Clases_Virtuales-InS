import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from courses.models import Course

User = get_user_model()

@pytest.mark.django_db
def test_teacher_can_create_course(client):
    teacher = User.objects.create_user("profe", password="123", role=User.Role.TEACHER)
    client.login(username="profe", password="123")
    url = reverse("courses:course_create")
    resp = client.post(url, {"title": "Álgebra", "description": "Intro"})
    assert resp.status_code == 302
    assert Course.objects.filter(title="Álgebra").exists()
