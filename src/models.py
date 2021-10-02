from database   import Base
from sqlalchemy import Column, String


class UserAdmin(Base):
    __tablename__   = 'useradmin'
    email           = Column(String, primary_key = True)
    contraseña      = Column(String)
    nombre          = Column(String)
    apellido        = Column(String)

