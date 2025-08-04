from django.views.generic import ListView, DetailView, TemplateView
from .models import Course, Enrollment

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    paginate_by = 6

class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"

class MyCoursesView(TemplateView):
    template_name = "courses/my_courses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["enrollments"] = Enrollment.objects.select_related("course").filter(
            student=self.request.user
        )
        return context
