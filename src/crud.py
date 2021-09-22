from    sqlalchemy.orm import Session
import  schema, models

def save_usuario_info(db: Session, info: schema.Usuario):
    device_info_model = models.Usuario(**info.dict())
    db.add(device_info_model)
    db.commit()
    db.refresh(device_info_model)
    return device_info_model

def get_usuario_info(db: Session, idusuario: str = None):
    if idusuario is None:
        return db.query(models.Usuario).all()
    else:
        return db.query(models.Usuario).filter(models.Usuario.idusuario == idusuario).first()

def error_message(message):
    return {
        'error': message
    }