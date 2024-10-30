from fastapi import APIRouter

from .ml_model.views import router as ml_router


router = APIRouter()


router.include_router(router=ml_router, prefix="/ml")
