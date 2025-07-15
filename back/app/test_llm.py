from llm import generate_matching

cv = """
Expériences : Chef de projet digital Crédit Agricole Nord de France; Conseiller clientèle Ma French Bank ; Conseiller de vente Leroy Merlin ; 

Compétences clés : Langages de programmation et bibliothèques : Python, SQL, Pandas, NumPy, Pytest
Frameworks de machine learning et IA : Scikit-learn, TensorFlow, Keras, PyTorch, LangChain, OpenCV
Big data et ingénierie des données : PySpark, Hadoop HDFS, Azure Data Lake Storage 
Plateformes cloud et services : Microsoft Azure (certification AZ900 et AI900)
Développement web et APIs : HTML/CSS, Tailwind, Django, Streamlit, Gradio, FastAPI, LangServe
Outils DevOps et CI/CD : Git, GitHub, GitHub Actions, Docker
Outils de scraping et extraction de données : Scrapy, Beautiful Soup, Selenium, Requests
Bases de données et ORMs : MySQL, PostgreSQL, SQLite, MongoDB, DuckDB, SQLAlchemy, SQLModel
Systèmes d'exploitation et commandes : Linux, Windows, commandes Unix, script Bash
Méthodes agiles et outil : Scrum, Kanban, Jira

Formation : Développeur Data IA, Master 2 Commerce Marketing, Licence Économie Gestion"""

job = """
Tu es titulaire d'un diplôme de niveau Bac+5 en statistiques décisionnelles et tu as une expérience d'au moins 5 ans en exploitation statistiques de données clients (datamining/études statistiques) idéalement au sein de Directions Marketing dans un environnement cross-canal, sur une mission similaire.   Tu es en capacité de faire des modélisations statistiques et mathématiques, et d'analyser des données dans un environnement Big Data, tu maîtrises les outils et langages statistiques et de data science : SQL, Python, R, Qlikview, Excel.    L'essentiel ? Tu souhaites allier tes passions pour le commerce et la donnée. Ta capacité d'analyse et de synthèse seront un atout pour répondre de la meilleure manière possible aux attentes de nos clients.      Le petit plus ? Tu as une appétence pour le secteur du retail et notamment du drive."""

result = generate_matching(cv, job)

print("Résultat final :", result)
