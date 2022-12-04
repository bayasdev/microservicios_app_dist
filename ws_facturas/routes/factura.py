from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
from config.db import conn
from models.factura import facturas
from schemas.factura import Factura, FacturaCreate

factura = APIRouter()


@factura.get('/facturas', response_model=List[Factura], tags=['facturas'])
def get_facturas():
    return conn.execute(facturas.select()).fetchall()


@factura.post('/facturas', response_model=Factura, tags=['facturas'])
def create_factura(factura: FacturaCreate):
    result = conn.execute(facturas.insert().values(factura.dict()))
    return conn.execute(facturas.select().where(facturas.c.id == result.inserted_primary_key[0])).first()


@factura.get('/facturas/{id}', response_model=Factura, tags=['facturas'])
def get_factura(id: str):
    return conn.execute(facturas.select().where(facturas.c.id == id)).first()


@factura.delete('/facturas/{id}', status_code=HTTP_204_NO_CONTENT, tags=['facturas'])
def delete_factura(id: str):
    conn.execute(facturas.delete().where(facturas.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@factura.put('/facturas/{id}', response_model=Factura, tags=['facturas'])
def update_factura(id: str, factura: FacturaCreate):
    conn.execute(facturas.update().values(factura.dict()).where(facturas.c.id == id))
    return conn.execute(facturas.select().where(facturas.c.id == id)).first()
