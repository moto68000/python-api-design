# 1. Base oficial de Python ligera
FROM python:3.13-slim

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /code

# 3. Variables de entorno críticas para Python en contenedores
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4. Dependencias del sistema nativas para evitar fallos con librerías de C/Postgres
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Copiar requerimientos e instalarlos usando la caché de Docker
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /code/requirements.txt

# 6. Copiar el código de la aplicación
COPY ./app /code/app

# 7. Comando de arranque para desarrollo (escuchando en todas las interfaces)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
