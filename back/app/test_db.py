from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Remplace par ta chaîne de connexion
DATABASE_URL = "postgresql://postgres:password@localhost:5432/Perfect_Match"

def test_connection():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Connexion réussie :", result.scalar())
    except SQLAlchemyError as e:
        print("Erreur de connexion :", e)

if __name__ == "__main__":
    test_connection()
