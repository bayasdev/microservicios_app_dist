from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Factura(BaseModel):
    id: int
    id_cliente: int
    fecha: datetime
    
class FacturaCreate(BaseModel):
    id_cliente: int
    fecha: datetime
