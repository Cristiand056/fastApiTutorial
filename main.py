from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/url")
async def ruta1():
    return {"url": "https://link_inventado"}