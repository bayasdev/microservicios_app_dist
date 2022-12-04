from pydantic import BaseModel


class DetalleFactura(BaseModel):
    id: int
    id_factura: int
    id_producto: int
    cantidad: int
    precio: float
    
class DetalleFacturaCreate(BaseModel):
    id_factura: int
    id_producto: int
    cantidad: int
    precio: float
