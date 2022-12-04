from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from typing import List
from config.db import conn
from models.producto import productos
from schemas.producto import Producto, ProductoCreate

producto = APIRouter()


@producto.get('/productos', response_model=List[Producto], tags=['productos'])
def get_productos():
    return conn.execute(productos.select()).fetchall()


@producto.post('/productos', response_model=Producto, tags=['productos'])
def create_producto(producto: ProductoCreate):
    result = conn.execute(productos.insert().values(producto.dict()))
    return conn.execute(productos.select().where(productos.c.id == result.inserted_primary_key[0])).first()


@producto.get('/productos/{id}', response_model=Producto, tags=['productos'])
def get_producto(id: str):
    return conn.execute(productos.select().where(productos.c.id == id)).first()


@producto.delete('/productos/{id}', status_code=HTTP_204_NO_CONTENT, tags=['productos'])
def delete_producto(id: str):
    conn.execute(productos.delete().where(productos.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@producto.put('/productos/{id}', response_model=Producto, tags=['productos'])
def update_producto(id: str, producto: ProductoCreate):
    conn.execute(productos.update().values(producto.dict()).where(productos.c.id == id))
    return conn.execute(productos.select().where(productos.c.id == id)).first()
