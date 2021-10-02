from    sqlalchemy.orm import Session
import  schema, models

def save_user_info(db: Session, info: schema.UserAdminJSON):
    user_info_model = models.UserAdmin(**info.dict())
    db.add(user_info_model)
    db.commit()
    db.refresh(user_info_model)
    return user_info_model

def get_user_info(db: Session, email: str = None):
    if email is None:
        return db.query(models.UserAdmin).all()
    else:
        return db.query(models.UserAdmin).filter(models.UserAdmin.email == email).first()

def error_message(message):
    return {
        'error': message
    }