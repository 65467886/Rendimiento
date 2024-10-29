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
