from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class UserDB(User):
    password: str
    
user_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Jose Jose",
        "email": "Jjose@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Jose Jose2",
        "email": "Jjose2@gmail.com",
        "disabled": True,
        "password": "654321"
    },
    
}

def search_user(username: str):
    if username in user_db:
        return UserDB(user_db[username])