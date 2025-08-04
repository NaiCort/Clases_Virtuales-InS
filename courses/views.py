from django.contrib import messages                      # NEW
from django.contrib.auth.decorators import login_required # NEW
from django.contrib.auth.mixins import LoginRequiredMixin # NEW
from django.shortcuts import get_object_or_404, redirect  # NEW
from django.urls import reverse_lazy                      # NEW
from django.views.generic import ListView, DetailView, TemplateView

from .models import Course, Enrollment


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    paginate_by = 6


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"


class MyCoursesView(LoginRequiredMixin, TemplateView):  # ← ahora exige login
    login_url = reverse_lazy("login")                   # redirige si no está autenticado
    template_name = "courses/my_courses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["enrollments"] = (
            Enrollment.objects.select_related("course")
            .filter(student=self.request.user)
        )
        return context


# --------------------------------------------------------------------
# Acción de inscripción
# --------------------------------------------------------------------
@login_required(login_url=reverse_lazy("login"))
def enroll_course(request, slug):
    course = get_object_or_404(Course, slug=slug)

    # Solo estudiantes pueden inscribirse
    if not getattr(request.user, "is_student", False):
        messages.info(request, "Solo los estudiantes pueden inscribirse.")
        return redirect("courses:course_detail", slug=slug)

    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course,
        defaults={"status": Enrollment.ACTIVE},
    )

    if created:
        messages.success(request, "¡Inscripción exitosa!")
    else:
        messages.warning(request, "Ya estabas inscrito en este curso.")

    return redirect("courses:my_courses")
