import  uvicorn
import  os
import  crud
from    fastapi        import FastAPI, Depends, HTTPException
from    database       import SessionLocal
from    schema         import UserAdminJSON

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

@app.post('/user')
def save_user(info: UserAdminJSON, db=Depends(db)):
    object_in_db = crud.get_user_info(db, info.email)
    if object_in_db:
        raise HTTPException(400, detail= crud.error_message("user already exists"))
    return crud.save_user_info(db,info)

@app.get('/user/{email}')
def get_user_info(email: str, db=Depends(db)):
    info = crud.get_user_info(db,email)
    if info:
        return info
    else:
        raise HTTPException(404, crud.error_message('user doest exist'))

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=int(os.environ.get('PORT')), reload=True)        
