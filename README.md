# API To-Do con FastAPI y Frontend minimalista
Un proyecto práctico para aprender el desarrollo backend con **FastAPI** y su conexión con un frontend sencillo.

### Tecnologías usadas
    Python / FastAPI: Para construir la API REST y validar datos con Pydantic.
    Uvicorn: Servidor ASGI para correr la aplicación.
    HTML5 / JavaScript: Interfaz visual básica para consumir los endpoints.

### Cómo ejecutar el proyecto localmente

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/lebronvargas2-hash/lista-de-tareas.git
   cd lista-de-tares/
2. Crear y activar el entorno virtual:
    En Windows(Git Bash): 
    python -m venv venv
    source venv/Scripts/activate
    - En linux/Mac:
    source venv/bin/activate
3. Instalar dependencias:
    pip install -r requirements.txt
4. Correr el servidor
    uvicorn main:app --reload
5. Abrir la aplicacion
    Entra a la documentacion -> http:127.0.0.1:8000/docs
    O abre el archivo index.html en el navegador