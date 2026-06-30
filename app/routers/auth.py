from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# Importamos correctamente tus módulos locales
from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    # 1. Corregido models.User (en singular) para buscar en la base de datos
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )

    # 2. Corregido utils.verify (con 's') para validar contra el nuevo hash nativo de bcrypt
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        ) 

    # 3. Corregido user.id (decías 'used.id') y apuntamos al módulo oauth2 correcto
    access_token = oauth2.create_acces_token(data={"user_id": user.id})    

    return {"access_token": access_token, "token_type": "bearer"}