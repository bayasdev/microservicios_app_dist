from pydantic import BaseModel


class Producto(BaseModel):
    id: int
    nombre: str
    descripcion: str
    tipo_producto: int
    precio: float
    
class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str
    tipo_producto: int
    precio: float
