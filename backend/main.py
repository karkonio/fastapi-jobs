from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.core.config import settings
from backend.apis.general_pages.route_homepage import general_pages_router
from backend.db.session import engine
from backend.db.base_class import Base

BASE_PATH = Path(__file__).resolve().parent


def include_router(app):
	app.include_router(general_pages_router)


def configure_static(app):  #new
    app.mount(
		"/static",
		StaticFiles(directory=str(BASE_PATH / "static")),
		name="static"
	)


def create_tables():           #new
	Base.metadata.create_all(bind=engine)


def start_application():
	print(f'------THE settings : {settings.POSTGRES_USER} and {settings.POSTGRES_PASSWORD}')
	print(f'------THE settings : {settings.POSTGRES_SERVER} and {settings.POSTGRES_PORT}')
	print(f'------THE settings : {settings.POSTGRES_DB} and {settings.DATABASE_URL}')
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
