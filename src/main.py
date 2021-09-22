from fastapi        import FastAPI, Depends, HTTPException
from database       import SessionLocal
from schema         import Usuario
import crud

app = FastAPI()

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return "Web Server UP"

@app.post('/usuario')
def save_usuario(info: Usuario, db=Depends(db)):
    object_in_db = crud.get_usuario_info(db, info.idusuario)
    if object_in_db:
        raise HTTPException(400, detail= crud.error_message('El usuario ya existe'))
    return crud.save_usuario_info(db,info)

@app.get('/usuario/{idusuario}')
def get_usuario_info(idusuario: str, db=Depends(db)):
    info = crud.get_usuario_info(db,idusuario)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('idusuario inexistente.'.format(idusuario)))        