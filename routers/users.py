from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

#Iniciar el server uvicorn users:app --reload

#entidad user

class User(BaseModel):
    id: int
    name: str 
    surname: str
    url: str
    age: int

users_list = [User(id=0, name="Brains", surname="Moure", url="https://moure.dev", age=35),
              User(id=1,name="Brains1", surname="Moure1", url="https://moure1.dev", age=36),
              User(id=2,name="Brains2", surname="Moure2", url="https://moure2.dev", age=37)]

async def usersjson():
    return [{"name": "Brais", "surname":"moure","url":"https://moures.dev", "edad":35},
            {"name": "Moure", "dev":"moure","url":"https://moures.com", "edad":35},
            {"name": "Brais2", "surname":"moure2","url":"https://moures2.dev", "edad":35}
            ]

@router.get("/users")
async def users():
    return users_list

#Path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id=id)
    
#Query
@router.get("/user/")
async def user(id: int):
    return search_user(id=id)

@router.post("/user/", response_model=User , status_code=201)
async def user(user: User):   
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
     
    users_list.append(user)
    return user

@router.put("/user/")
async def user(user: User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return {"Error":"No se ha encontrado el usuario a actulizar"}
    
    return user

@router.delete("/user/{id}")
async def user(id: int):
    deleted = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            deleted = True
            return{"Mensaje":"Usuario Borrado con exito"}
    
    if not deleted:
        return{"Error":"Fallo el Borrado del usuario"} 
      
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"El Id no se encontra"}
    
