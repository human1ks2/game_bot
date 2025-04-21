from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import os

# Абсолютный путь к текущей директории — webapp/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Абсолютный путь к static и templates
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Проверка существования папок (как разработчик — логируем)
if not os.path.exists(STATIC_DIR):
    raise RuntimeError(f"Статическая папка не найдена: {STATIC_DIR}")
if not os.path.exists(TEMPLATES_DIR):
    raise RuntimeError(f"Папка шаблонов не найдена: {TEMPLATES_DIR}")

# Инициализация FastAPI
app = FastAPI()

# Монтируем статику
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Настройка шаблонов
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Возвращает HTML страницу с игрой.
    """
    return templates.TemplateResponse("index.html", {"request": request})
