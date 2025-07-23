from django.urls import path
from .views import register_view, login_view, load_cv_view, matching_view, logout_view
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path('matching/', matching_view, name='matching'),
    path('load_cv/', load_cv_view, name='load_cv'),
    path('auth/register/', register_view, name='register'),
    path("auth/login/", login_view, name="login"),
    path('', TemplateView.as_view(template_name="index.html")),
    path("logout/", logout_view, name="logout")

    ]