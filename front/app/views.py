# from django.views.generic import TemplateView
# from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, User
import requests
from django.views.decorators.csrf import csrf_exempt



def home_view(request):
    return render(request, 'home.html')

@csrf_exempt
def register_view(request):
    print("register_view appelée")
    print("REQUÊTE REÇUE :", request.method)

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password1")
        password_confirm = request.POST.get("password2")

        print(f"Inscription : {username} / {email}")

        # Vérifications basiques
        if not username or not email or not password or not password_confirm:
            return render(request, "register.html", {
                "error_message": "Tous les champs sont obligatoires."
            })

        if password != password_confirm:
            return render(request, "register.html", {
                "error_message": "Les mots de passe ne correspondent pas."
            })

        # Prépare les données à envoyer à FastAPI
        register_data = {
            "username": username,
            "email": email,
            "password": password,
        }

        url = "http://127.0.0.1:8001/auth/register/"

        try:
            response = requests.post(url, json=register_data)
            print("Status code FastAPI :", response.status_code)
            print("Réponse FastAPI :", response.text)

            if response.status_code == 200:
                return redirect("login")
            else:
                # Gestion d’erreur avec message reçu de l’API
                try:
                    error_data = response.json()
                    error_message = error_data.get("detail", "Erreur lors de l'inscription.")
                except Exception:
                    error_message = "Erreur lors de l'inscription."

                return render(request, "register.html", {
                    "error_message": error_message
                })

        except requests.exceptions.RequestException as e:
            print("Erreur lors de la requête FastAPI :", e)
            return render(request, "register.html", {
                "error_message": "Impossible de contacter le serveur d'inscription."
            })

    # Si GET, afficher le formulaire d'inscription
    return render(request, "register.html")


@csrf_exempt
def login_view(request):

    if request.method == "POST":
        print("POST reçu")
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(f"Tentative de connexion avec : {username} / {password}")

        if not username or not password:
            print("Erreur : champs manquants")
            return render(request, "login.html", {"error": "Champs manquants."})

        login_data = {"username": username, "password": password}
        url = "http://127.0.0.1:8001/auth/login/"

        response = requests.post(url, json=login_data)

        print("Status code de la réponse FastAPI :", response.status_code)
        print("Contenu brut de la réponse FastAPI :", response.text)

        if response.status_code == 200:
            try:
                data = response.json()
                print("Données JSON reçues :", data)
                token = data.get("access_token")
                if token:
                    print("Token reçu, stockage en session et redirection")
                    request.session["token"] = token
                    return redirect("load_cv")
                else:
                    error = "Token manquant dans la réponse."
                    print("Erreur :", error)
            except Exception as e:
                error = f"Erreur JSON : {str(e)}"
                print(error)
        else:
            error = "Identifiant ou mot de passe incorrect."
            print("Erreur :", error)

        return render(request, "login.html", {"error": error})

    return render(request, "login.html")

from django.contrib import messages

@csrf_exempt  # Si tu n'as pas de token CSRF côté FastAPI
def load_cv_view(request):
    if request.method == "POST":
        cv_text = request.POST.get("cv_text")
        secteur = request.POST.get("secteur")

        if not cv_text or not secteur:
            return render(request, "load_cv.html", {
                "error_message": "Tous les champs sont obligatoires.",
                "cv_text": cv_text,
                "secteur": secteur
            })

        # Prépare les données au format attendu par ton API FastAPI
        data = {
            "cv_text": cv_text,
            "secteur": secteur
        }

        url = "http://127.0.0.1:8001/load_cv"  # Adapte l’URL si besoin

        try:
            response = requests.post(url, json=data)
            if response.status_code == 201 or response.status_code == 200:
                # Succès
                return render(request, "load_cv.html", {
                    "success_message": "CV enregistré avec succès !"
                })
            else:
                # Erreur retournée par FastAPI
                error = response.json().get("detail", "Erreur lors de l'enregistrement.")
                return render(request, "load_cv.html", {
                    "error_message": error,
                    "cv_text": cv_text,
                    "secteur": secteur
                })
        except requests.exceptions.RequestException as e:
            return render(request, "load_cv.html", {
                "error_message": "Impossible de contacter le serveur.",
                "cv_text": cv_text,
                "secteur": secteur
            })

    # GET = affichage formulaire vide
    return render(request, "load_cv.html")





# def matching_view(request):
#     # Si tu veux appeler ton API FastAPI pour récupérer les résultats de matching
#     try:
#         response = requests.get("http://localhost:8001/matching")
#         if response.status_code == 200:
#             data = response.json()
#         else:
#             data = {"error": "Erreur lors de la récupération des résultats"}
#     except requests.exceptions.ConnectionError:
#         data = {"error": "L'API FastAPI ne répond pas"}

#     return render(request, "matching.html", {"data": data})