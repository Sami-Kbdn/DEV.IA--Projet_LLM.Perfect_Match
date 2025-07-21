from django.urls import path
from .views import register_view, login_view
from django.views.generic import TemplateView
from django.urls import path
# matching_views, LogoutView, LoginView,

urlpatterns = [
    # path('matching/', matching_view, name='matching'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', TemplateView.as_view(template_name="index.html"))

    ]