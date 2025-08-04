from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Course, Lesson
from .forms import CourseForm, LessonForm

class TeacherRequiredMixin(UserPassesTestMixin):
    """Permite el paso sólo a usuarios con rol docente o superior."""

    def test_func(self):
        return getattr(self.request.user, "is_teacher", False)

    def handle_no_permission(self):
        from django.contrib import messages
        messages.error(self.request, "No tienes permisos para acceder a esta página.")
        return super().handle_no_permission()

# ---------- Cursos ----------

class MyTeacherCoursesView(LoginRequiredMixin, TeacherRequiredMixin, ListView):
    template_name = "courses/teacher_course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        return self.request.user.courses.all()

class CourseCreateView(LoginRequiredMixin, TeacherRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super().form_valid(form)

class CourseUpdateView(LoginRequiredMixin, TeacherRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"

class CourseDeleteView(LoginRequiredMixin, TeacherRequiredMixin, DeleteView):
    model = Course
    template_name = "courses/course_confirm_delete.html"
    success_url = reverse_lazy("courses:teacher_course_list")

# ---------- Lecciones ----------

class LessonCreateView(LoginRequiredMixin, TeacherRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = "courses/lesson_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.course = Course.objects.get(slug=kwargs["slug"])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.course = self.course
        return super().form_valid(form)

    def get_success_url(self):
        return self.course.get_absolute_url()  # asegúrate de tener este método

class LessonUpdateView(LoginRequiredMixin, TeacherRequiredMixin, UpdateView):
    model = Lesson
    form_class = LessonForm
    template_name = "courses/lesson_form.html"

    def get_success_url(self):
        return self.object.course.get_absolute_url()

class LessonDeleteView(LoginRequiredMixin, TeacherRequiredMixin, DeleteView):
    model = Lesson
    template_name = "courses/lesson_confirm_delete.html"

    def get_success_url(self):
        return self.object.course.get_absolute_url()
