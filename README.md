# Proyecto de Monitoreo de Rendimiento del Sistema con FastAPI

Este proyecto utiliza FastAPI para crear una API que monitorea el rendimiento del sistema. A continuación se presentan los códigos necesarios para implementar la aplicación.

## 1. Código HTML: `index.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monitoreo de Rendimiento del Sistema</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h1 {
            color: #4CAF50;
            margin-bottom: 20px;
        }

        .status-container {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 300px;
            text-align: center;
        }

        .status {
            font-size: 1.2em;
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        .status:hover {
            background-color: #f0f0f0;
        }

        footer {
            margin-top: 30px;
            font-size: 0.8em;
            color: #777;
        }

        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            cursor: pointer;
            font-size: 1em;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #45a049;
        }
    </style>
    <script>
        async function fetchStatus() {
            const response = await fetch("http://127.0.0.1:8000/status");
            const data = await response.json();
            document.getElementById("cpu").innerText = `Uso de CPU: ${data.cpu_usage}%`;
            document.getElementById("memory").innerText = `Uso de Memoria: ${data.memory_usage}%`;
            document.getElementById("disk").innerText = `Uso de Disco: ${data.disk_usage}%`;
        }

        function startMonitoring() {
            fetchStatus();
            setInterval(fetchStatus, 5000); // Actualizar cada 5 segundos
        }
    </script>
</head>
<body onload="startMonitoring()">
    <h1>Monitoreo de Rendimiento del Sistema</h1>
    <div class="status-container">
        <p id="cpu" class="status">Uso de CPU: Cargando...</p>
        <p id="memory" class="status">Uso de Memoria: Cargando...</p>
        <p id="disk" class="status">Uso de Disco: Cargando...</p>
        <button onclick="fetchStatus()">Actualizar Ahora</button>
    </div>
    <footer>
        <p>Monitoreo en tiempo real del rendimiento del sistema.</p>
    </footer>
</body>
</html>
```

## 2. Código Python: `main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel
import psutil

app = FastAPI()

class SystemStatus(BaseModel):
    cpu_usage: float
    memory_usage: float
    disk_usage: float

@app.get("/status", response_model=SystemStatus)
async def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "disk_usage": disk_usage
    }

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)
```

## 3. Crear y Ejecutar un Entorno Virtual

1. Asegúrate de tener Python instalado en tu máquina.
2. Abre una terminal y navega al directorio donde quieres crear tu proyecto.
3. Crea un entorno virtual ejecutando el siguiente comando:
   ```bash
   python -m venv env
   ```
4. Activa el entorno virtual:
   - En **Windows**:
     ```bash
     .\env\Scriptsctivate
     ```
   - En **macOS y Linux**:
     ```bash
     source env/bin/activate
     ```
5. Instala las dependencias necesarias ejecutando:
   ```bash
   pip install fastapi uvicorn psutil
   ```
6. Guarda el código HTML en un archivo llamado `index.html` y el código Python en `main.py`.
7. Ejecuta la aplicación FastAPI con el siguiente comando:
   ```bash
   uvicorn main:app --reload
   ```
8. Abre tu navegador y dirígete a `http://127.0.0.1:8000` para ver la interfaz de monitoreo.

