from fastapi import FastAPI

app = FastAPI(title="API para estudos",
    description="API para estudos e testes de FastAPI",
    version="1.0.0",
    contact={
        "name": "João Pedro",
        "email": "lourencodossantosjoaopedro@gmail.com"
    })