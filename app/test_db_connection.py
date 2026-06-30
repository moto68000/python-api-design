import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def test_supabase_connection():
    # Obtenemos la URL de los secretos de GitHub o del .env
    db_url = f"postgresql://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOSTNAME')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
    
    try:
        engine = create_engine(db_url)
        with engine.connect() as connection:
            # Una consulta simple para verificar que la base responde
            result = connection.execute(text("SELECT 1"))
            assert result.scalar() == 1
            print("¡Conexión exitosa a Supabase!")
    except SQLAlchemyError as e:
        print(f"Error de conexión: {e}")
        assert False