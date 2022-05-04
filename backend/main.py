from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.core.config import settings
from backend.apis.base import api_router
from backend.db.session import engine
from backend.db.base import Base

BASE_PATH = Path(__file__).resolve().parent


def include_router(app):
	app.include_router(api_router)


def configure_static(app):
    app.mount(
		"/static",
		StaticFiles(directory=str(BASE_PATH / "static")),
		name="static"
	)


def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)


def start_application():
	app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION
    )


	include_router(app)
	configure_static(app)
	create_tables()
	return app


app = start_application()


# @app.get("/")
# def hello_api():
#     return {"msg":"Hello API"}
