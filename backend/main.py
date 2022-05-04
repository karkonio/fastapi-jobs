from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.core.config import settings
from backend.apis.general_pages.route_homepage import general_pages_router

BASE_PATH = Path(__file__).resolve().parent


def include_router(app):
	app.include_router(general_pages_router)


def configure_static(app):  #new
    app.mount(
		"/static",
		StaticFiles(directory=str(BASE_PATH / "static")),
		name="static"
	)


def start_application():
	app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )
	include_router(app)
	configure_static(app)
	return app


app = start_application()


# @app.get("/")
# def hello_api():
#     return {"msg":"Hello API"}
