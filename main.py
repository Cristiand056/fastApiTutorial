from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

#Iniciar el server uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def ruta1():
    return {"url": "https://link_inventado"}

# Documentación con Swagger: http:...../docs
# Documentación con Redocl: http:...../redoc