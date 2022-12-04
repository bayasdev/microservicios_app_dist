from sqlalchemy import create_engine, MetaData
from config.config import settings

engine = create_engine(
    f'postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_SERVER}:{settings.DB_PORT}/{settings.DB_NAME}')

meta = MetaData()

conn = engine.connect()
