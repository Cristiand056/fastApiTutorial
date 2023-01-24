from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"menssage":"No encontrado"}}
                   )

#Iniciar el server uvicorn products:app --reload

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
    return ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/{id}")
async def products(id: int):
    return products_list[id]