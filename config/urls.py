# config/urls.py
from django.contrib import admin
from django.urls import path, include          # ← AQUI está 'path'
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect          # (si vas a usar la vista root opcional)

# ------------- OPCIONAL: vista root que redirige a cursos -------------
def root(request):
    return redirect("courses:course_list")
# ----------------------------------------------------------------------

urlpatterns = [
    path("admin/", admin.site.urls),

    # App de cursos
    path("courses/", include("courses.urls")),

    # Ruta raíz provisional
    path("", root, name="home"),          # o cámbiala por TemplateView / home.html

    # Autenticación
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
]
