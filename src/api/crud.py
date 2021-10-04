from    sqlalchemy.orm import Session
import  schema, models

def get_user_info(db: Session, email: str = None):
    if email is not None:
        return db.query(models.UserAdmin).filter(models.UserAdmin.email == email).first()
    
def get_users_info(db: Session):
    return db.query(models.UserAdmin).all() 
        
def get_user_login(db: Session, email: str = None, contraseña: str = None):
    if ((email is not None) and (contraseña is not None)):
        return db.query(models.UserAdmin).filter(models.UserAdmin.email == email).filter(models.UserAdmin.contraseña == contraseña).first()
        
def save_user_info(db: Session, info: schema.UserAdminJSON):
    user_info_model = models.UserAdmin(**info.dict())
    db.add(user_info_model)
    db.commit()
    db.refresh(user_info_model)
    return user_info_model

def error_message(message):
    return {
        'error': message
    }