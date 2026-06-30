from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings  # Importación corregida

# Imprime la contraseña de la BD en consola para verificar que lea el archivo .env
print(settings.database_password)

# Crea las tablas en Postgres si no existen (mientras no usemos migraciones automáticas)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclusión de routers limpian la arquitectura
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Daaamn i'm looking good"}