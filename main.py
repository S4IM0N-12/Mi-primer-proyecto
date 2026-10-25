from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Tarea(BaseModel):
    titulo: str
    descripcion: str
base_de_datos_tareas = []
@app.get("/")
def inicio():
    return {"mensaje": "API de notas lista"}


@app.get("/tareas")
def obtener_tareas():
    return {"total": len(base_de_datos_tareas), "tareas": base_de_datos_tareas}


@app.post("/tareas")
def crear_tareas(tarea: Tarea):
    base_de_datos_tareas.append(tarea)
    return {"mensaje": "Tarea creada con exito", "tarea guardad": tarea}