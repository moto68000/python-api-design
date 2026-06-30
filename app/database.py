import time
import psycopg
from psycopg.rows import dict_row
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # Necesitamos esto para la sesión
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

# 1. URL de conexión
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# 2. Motor y Fábrica de sesiones
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Base declarativa
Base = declarative_base()

# 4. LA FUNCIÓN QUE TE FALTA: La dependencia para tus routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. Validación de conexión (Psycopg)
while True:
    try:
        conn = psycopg.connect(
            host=settings.database_hostname,
            dbname=settings.database_name,
            user=settings.database_username,
            password=settings.database_password,
            port=settings.database_port,
            row_factory=dict_row
        )
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to the database failed")
        print("Error: ", error)
        time.sleep(2)