from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.config import settings
from routes.factura import factura
from routes.detalle_factura import detalle_factura

app = FastAPI(
    title='WS Facturas',
    description='Microservicio de Facturas',
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
    return {'msg': 'WS Facturas Operativo'}

app.include_router(factura)

app.include_router(detalle_factura)

if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=settings.PORT, reload=True)
