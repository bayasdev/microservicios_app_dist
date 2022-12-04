from typing import Optional
from pydantic import BaseModel


class TipoProducto(BaseModel):
    id: int
    nombre: str
    
class TipoProductoCreate(BaseModel):
    nombre: str
