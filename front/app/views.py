import requests
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

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

        if not username or not email or not password or not password_confirm:
            return render(request, "register.html", {
                "error_message": "Tous les champs sont obligatoires."
            })

        if password != password_confirm:
            return render(request, "register.html", {
                "error_message": "Les mots de passe ne correspondent pas."
            })

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

    return render(request, "register.html")

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        login_data = {"username": username, "password": password}
        url = "http://127.0.0.1:8001/auth/login/"

        

        try:
            response = requests.post(url, json=login_data)
            if response.status_code == 200:
                token = response.json().get("access_token")
                request.session["token"] = token
                return redirect("load_cv") 
            else:
                error_message = response.json().get("detail", "Erreur de connexion.")
                return render(request, "login.html", {"error_message": error_message})
        except requests.exceptions.RequestException:
            return render(request, "login.html", {"error_message": "Serveur inaccessible."})

    return render(request, "login.html")

def logout_view(request):
    request.session.pop("token", None)
    return redirect("/")

@csrf_exempt
def load_cv_view(request):
    print("Début de load_cv_view")

    token = request.session.get("token")
    print(f"Token récupéré : {token}")

    if request.method == "POST":
        print("Méthode POST détectée")

        cv_text = request.POST.get("cv_text")
        sector = request.POST.get("sector")
        print(f"cv_text: {cv_text}, secteur: {sector}")

        if not cv_text or not sector:
            print("Champs manquants")
            return render(request, "load_cv.html", {
                "error_message": "Tous les champs sont obligatoires.",
                "cv_text": cv_text,
                "sector": sector,
                "token": token,  
            })

        if not token:
            print("Pas de token, redirection vers login")
            return redirect("register")

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        data = {
            "cv_text": cv_text,
            "sector": sector
        }

        print("Données envoyées à FastAPI :", data)

        try:
            response = requests.post("http://127.0.0.1:8001/load_cv/", json=data, headers=headers)
            print("Réponse FastAPI :", response.status_code, response.text)
        except Exception as e:
            print("Erreur lors de la requête à FastAPI :", e)
            return render(request, "load_cv.html", {
                "error_message": "Erreur de connexion à l'API.",
                "cv_text": cv_text,
                "sector": sector,
                "token": token,  
            })

        if response.status_code == 200:
            print("Redirection vers le matching")
            return redirect("matching")
        else:
            print("Erreur côté FastAPI")
            return render(request, "load_cv.html", {
                "error_message": "Erreur lors de l'envoi à l'API.",
                "cv_text": cv_text,
                "sector": sector,
                "token": token,  
            })

    print("Méthode GET - affichage du formulaire")
    return render(request, "load_cv.html", {"token": token})

@csrf_exempt
def matching_view(request):
    token = request.session.get("token")
    is_authenticated = token is not None

    if not token:
        messages.error(request, "Utilisateur non connecté.")
        return redirect("login")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = None

    if request.method == "POST":
        job_description = request.POST.get("job_description")
        cv_id = request.POST.get("cv_id")

        payload = {
            "cv_id": int(cv_id),
            "job_description": job_description
        }

        try:
            response = requests.post("http://127.0.0.1:8001/matching/", json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
            else:
                messages.error(request, f"Erreur : {response.json().get('detail')}")
        except requests.exceptions.RequestException:
            messages.error(request, "Erreur de connexion à l'API")

    try:
        response = requests.get("http://127.0.0.1:8001/check_cv/", headers=headers)
        if response.status_code == 200:
            user_cvs = response.json()
        else:
            user_cvs = []
            messages.error(request, "Impossible de récupérer vos CV.")
    except requests.exceptions.RequestException:
        user_cvs = []
        messages.error(request, "Erreur de connexion à l'API pour récupérer les CV.")

    return render(request, "matching.html", {
        "user_cvs": user_cvs,
        "matching_result": data,
        "job_description": request.POST.get("job_description", ""),
        "cv_id": request.POST.get("cv_id", None),
        "is_authenticated": is_authenticated,
        "token": token,  
    })

