from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, Float
from config.db import meta, engine

productos = Table('productos', meta,
                 Column('id', Integer, primary_key=True),
                 Column('nombre', String(255)),
                 Column('descripcion', String(255)),
                 Column('tipo_producto', Integer, ForeignKey(
                     'tipo_productos.id', ondelete='CASCADE')),
                 Column('precio', Float),
                 )

meta.create_all(engine)
