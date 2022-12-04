from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import Integer, Float
from config.db import meta, engine

detalle_facturas = Table('detalle_facturas', meta,
                 Column('id', Integer, primary_key=True),
                 Column('id_factura', Integer, ForeignKey(
                     'facturas.id', ondelete='CASCADE')),
                 Column('id_producto', Integer),
                 Column('cantidad', Integer),
                 Column('precio', Float),
                 )

meta.create_all(engine)
