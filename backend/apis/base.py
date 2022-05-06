from fastapi import APIRouter

from backend.apis.version1 import route_general_pages
from backend.apis.version1 import route_users
from backend.apis.version1 import route_jobs
from backend.apis.version1 import route_login


api_router = APIRouter()


api_router.include_router(
    route_general_pages.general_pages_router, prefix="", tags=["General_pages"]
)
api_router.include_router(route_users.router, prefix="/users", tags=["Users"])
api_router.include_router(route_jobs.router, prefix="/jobs", tags=["Jobs"])
api_router.include_router(route_login.router, prefix="/login", tags=["Login"])
