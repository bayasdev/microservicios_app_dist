from sqlalchemy import DateTime, Table, Column
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta, engine
import datetime

facturas = Table('facturas', meta,
                 Column('id', Integer, primary_key=True),
                 Column('id_cliente', Integer),
                 Column('fecha', DateTime, default=datetime.datetime.now),
                 )

meta.create_all(engine)
