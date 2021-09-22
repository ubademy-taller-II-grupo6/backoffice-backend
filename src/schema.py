from pydantic   import BaseModel
from typing     import Optional

class Usuario (BaseModel):
    idusuario   :   str
    contraseña  :   Optional[str]
    nombre      :   Optional[str]
    apellido    :   Optional[str]
    email       :   Optional[str]

    class Config:
        orm_mode = True