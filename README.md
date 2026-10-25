# API To-Do con FastAPI y Frontend minimalista

Un proyecto práctico para aprender el desarrollo backend con **FastAPI** y su conexión con un frontend sencillo.

## Tecnologías usadas
* **Python / FastAPI**: Para construir la API REST y validar datos con Pydantic.
* **Uvicorn**: Servidor ASGI para correr la aplicación.
* **HTML5 / JavaScript**: Interfaz visual básica para consumir los endpoints.

## Cómo ejecutar el proyecto localmente

### En Windows (Git Bash):
```bash
git clone https://github.com/S4IM0N-12/lista-de-tareas.git
cd lista-de-tareas/
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
### En Linux/Mac:
```bash
git clone https://github.com/S4IM0N-12/lista-de-tareas.git
cd lista-de-tareas/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
### Uso:
1. Entra a la documentación interactiva en: http://127.0.0.1:8000/docs
2. O abre el archivo index.html en el navegador para usar la interfaz visual.