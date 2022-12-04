import datetime
from sqlalchemy import DateTime, Table, Column
from sqlalchemy.sql.sqltypes import Integer
# from sqlalchemy.orm import declarative_base, relationship
from config.db import meta, engine

facturas = Table('facturas', meta,
                 Column('id', Integer, primary_key=True),
                 Column('id_cliente', Integer),
                 Column('fecha', DateTime, default=datetime.datetime.now),
                 )

meta.create_all(engine)
