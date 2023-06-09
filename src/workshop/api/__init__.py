from fastapi import APIRouter
from .operations import router as operations_router
from .auth import router as auth_router
from .reports import router as reports_router
from .profile import router as profile_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(operations_router)
router.include_router(reports_router)
router.include_router(profile_router)