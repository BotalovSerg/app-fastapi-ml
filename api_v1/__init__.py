from fastapi import APIRouter

from .auth_user.views import router as auth_router
from .ml_model.views import router as ml_router


router = APIRouter()

router.include_router(router=auth_router, prefix="/auth")
router.include_router(router=ml_router, prefix="/ml")
