from django.views.generic import TemplateView
from django.contrib.auth import authenticate, logout
from django.shortcuts import render

# class MatchingView(TemplateView):
        
#         template_name = 'app/registration/login.html'
#         def post(self, request):
#             """Handles POST requests for login, authenticates user."""
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)


def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

