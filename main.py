from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI(
    title="User Management API",
    description="API для управления пользователями",
    version="0.1"
)


user_db = {} 


@app.post('/users/{phone}', response_model=User)
async def create_user(user: User):
    if user.phone in user_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_db[user.phone] = user
    return user




@app.get('/users/{phone}', response_model=User)
async def read_user(phone:str):
    user = user_db.get(phone)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@app.put('/users/{phone}', response_model=User)
async def update_user(phone:str, uodated_user: User):
    if phone not in user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_db[phone] = update_user
    return update_user


@app.delete('/users/{phone}')
async def delete_user(phone: str):
    if phone not in user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    del user_db[phone]
    return {'detail': "User is delete"}