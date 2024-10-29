from fastapi import APIRouter


router = APIRouter(tags=["ML Model"])


@router.get("/check/")
def get_status():
    return {"message": "ok"}