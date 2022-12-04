from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
from config.db import conn
from models.tipo_producto import tipo_productos
from schemas.tipo_producto import TipoProducto, TipoProductoCreate

tipo_producto = APIRouter()


@tipo_producto.get('/tipo_productos', response_model=List[TipoProducto], tags=['tipo_productos'])
def get_tipo_productos():
    return conn.execute(tipo_productos.select()).fetchall()


@tipo_producto.post('/tipo_productos', response_model=TipoProducto, tags=['tipo_productos'])
def create_tipo_producto(tipo_producto: TipoProductoCreate):
    result = conn.execute(tipo_productos.insert().values(tipo_producto.dict()))
    return conn.execute(tipo_productos.select().where(tipo_productos.c.id == result.inserted_primary_key[0])).first()


@tipo_producto.get('/tipo_productos/{id}', response_model=TipoProducto, tags=['tipo_productos'])
def get_tipo_producto(id: str):
    return conn.execute(tipo_productos.select().where(tipo_productos.c.id == id)).first()


@tipo_producto.delete('/tipo_productos/{id}', status_code=HTTP_204_NO_CONTENT, tags=['tipo_productos'])
def delete_tipo_producto(id: str):
    conn.execute(tipo_productos.delete().where(tipo_productos.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@tipo_producto.put('/tipo_productos/{id}', response_model=TipoProducto, tags=['tipo_productos'])
def update_tipo_producto(id: str, tipo_producto: TipoProductoCreate):
    conn.execute(tipo_productos.update().values(tipo_producto.dict()).where(tipo_productos.c.id == id))
    return conn.execute(tipo_productos.select().where(tipo_productos.c.id == id)).first()
