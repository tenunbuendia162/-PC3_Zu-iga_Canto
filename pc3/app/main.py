from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Numeros(BaseModel):
    valores: List[float]


@app.get("/sumar")
def sumar(a: int, b: int):
    return {"resultado": a + b}


@app.post("/promedio")
def promedio(datos: Numeros):
    if len(datos.valores) == 0:
        raise HTTPException(status_code=400, detail="Lista vacía")
    return {"promedio": sum(datos.valores) / len(datos.valores)}


@app.get("/health")
def health():
    return {"status": "ok"}
