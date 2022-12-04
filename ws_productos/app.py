from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.environment import settings
from routes.tipo_producto import tipo_producto
from routes.producto import producto

app = FastAPI(
    title='WS Productos',
    description='Microservicio de Productos',
    version='1.0',
)

# Middlewares

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes

@app.get('/')
def home():
    return {'msg': 'WS Productos Operativo'}

app.include_router(tipo_producto)

app.include_router(producto)

if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=settings.PORT, reload=True)
