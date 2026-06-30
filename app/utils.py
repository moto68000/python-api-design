import bcrypt

def hash(password: str) -> str:
    # 1. Convertimos el string de la contraseña a bytes (UTF-8)
    pwd_bytes = password.encode('utf-8')
    # 2. Generamos el salt (la semilla aleatoria de seguridad)
    salt = bcrypt.gensalt()
    # 3. Hasheamos y decodificamos a string para poder guardarlo en la base de datos
    return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')

def verify(plain_password: str, hashed_password: str) -> bool:
    # Comparamos los bytes de la contraseña que ingresa el usuario contra el hash guardado
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))