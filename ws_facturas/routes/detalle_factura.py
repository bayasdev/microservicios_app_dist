from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.detalle_factura import detalle_facturas
from schemas.detalle_factura import DetalleFactura, DetalleFacturaCreate

detalle_factura = APIRouter()


@detalle_factura.get('/detalle_facturas', tags=['detalle_facturas'])
def get_detalle_facturas():
    return conn.execute(detalle_facturas.select()).fetchall()


@detalle_factura.post('/detalle_facturas', response_model=DetalleFactura, tags=['detalle_facturas'])
def create_detalle_factura(detalle_factura: DetalleFacturaCreate):
    result = conn.execute(detalle_facturas.insert().values(detalle_factura.dict()))
    return conn.execute(detalle_facturas.select().where(detalle_facturas.c.id == result.inserted_primary_key[0])).first()


@detalle_factura.get('/detalle_facturas/{id}', response_model=DetalleFactura, tags=['detalle_facturas'])
def get_detalle_factura(id: str):
    return conn.execute(detalle_facturas.select().where(detalle_facturas.c.id == id)).first()


@detalle_factura.delete('/detalle_facturas/{id}', status_code=HTTP_204_NO_CONTENT, tags=['detalle_facturas'])
def delete_detalle_factura(id: str):
    conn.execute(detalle_facturas.delete().where(detalle_facturas.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@detalle_factura.put('/detalle_facturas/{id}', response_model=DetalleFactura, tags=['detalle_facturas'])
def update_detalle_factura(id: str, detalle_factura: DetalleFacturaCreate):
    conn.execute(detalle_facturas.update().values(detalle_factura.dict()).where(detalle_facturas.c.id == id))
    return conn.execute(detalle_facturas.select().where(detalle_facturas.c.id == id)).first()
