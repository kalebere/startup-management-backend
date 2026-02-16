from fastapi import APIRouter
from .v1.auth import router as auth_router
from .v1.dashboard import router as dashboard_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(dashboard_router)
