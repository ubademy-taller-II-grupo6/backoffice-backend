from pydantic   import BaseModel
from typing     import Optional

class UserAdminJSON (BaseModel):
    email       :   str
    contraseña  :   str
    nombre      :   Optional[str]
    apellido    :   Optional[str]

    class Config:
        orm_mode = True