from groq import Groq
import os
from dotenv import load_dotenv
import re
import json

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def generate_matching(cv_text: str, job_description: str) -> dict:
    """
    Appelle le modèle Groq pour comparer un CV et une offre.
    Retourne un JSON : {"score": int, "feedback": str}
    """

    user_prompt = f"""
Tu es un expert RH.
Compare le CV suivant :
{cv_text}

Avec cette offre d'emploi :
{job_description}

Compare :
- Les compétences techniques (50% du score)
- Le secteur d'activité (30%)
- L’adéquation du niveau général (20%)

Pour chaque point, vérifie les mots-clés similaires.
Donne un score de compatibilité entre 0 et 100 et rédige un feedback court.
Réponds STRICTEMENT en JSON :
{{ "score": int, "feedback": "..." }}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile", 
        messages=[
            {"role": "system", "content": "Tu es un expert RH."},
            {"role": "user", "content": user_prompt}
        ]
    )

    raw_text = response.choices[0].message.content.strip()
    print("LLM RAW OUTPUT:", raw_text)


    def extract_json(text):
        pattern = r'\{.*\}'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                return {"score": 0, "feedback": "Réponse JSON mal formée."}
        else:
            return {"score": 0, "feedback": "Pas de JSON détecté."}

    result = extract_json(raw_text)
    return result