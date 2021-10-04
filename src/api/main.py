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

@app.get('/user/')
def get_user_info(email:str, db=Depends(db)):
    user = crud.get_user_info(db,email)
    if user:
        return user
    else:
        raise HTTPException(404, crud.error_message('user doest exist'))

@app.get('/users/')
def get_users_info(db=Depends(db)):
    users = crud.get_users_info(db)
    if users:
        return users
    else:
        raise HTTPException(404, crud.error_message('there arent users'))    

@app.get('/login/')
def get_user_login(email: str, contraseña:str, db=Depends(db)):
    info = crud.get_user_login(db, email, contraseña)
    if info: 
        return info
    else:
        raise HTTPException(404, crud.error_message('user or password doest match'))

@app.post('/user/')
def save_user(info: UserAdminJSON, db=Depends(db)):
    user = crud.get_user_info(db, info.email)
    if user:
        raise HTTPException(400, detail= crud.error_message("user already exists"))
    return crud.save_user_info(db,info)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=int(os.environ.get('PORT')), reload=True)        
