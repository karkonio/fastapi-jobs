from pathlib import Path

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


BASE_PATH = Path(__file__).resolve().parent.parent.parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
    return TEMPLATES.TemplateResponse(
        "/general_pages/homepage.html",
        {"request": request}
    )
