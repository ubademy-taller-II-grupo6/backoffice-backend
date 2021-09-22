from database   import Base
from sqlalchemy import Column, String


class Usuario(Base):
    __tablename__   = 'usuariobackoffice'
    idusuario       = Column(String, primary_key = True)
    contraseña      = Column(String)
    nombre          = Column(String)
    apellido        = Column(String)
    email           = Column(String)

