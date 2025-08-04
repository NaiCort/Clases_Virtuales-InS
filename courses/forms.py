from django import forms
from .models import Course, Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ("title", "content", "order", "video_url")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
            "order": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "video_url": forms.URLInput(attrs={"class": "form-control"}),
        }
