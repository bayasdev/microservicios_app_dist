from typing import Optional
from pydantic import BaseModel
from datetime import datetime


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
