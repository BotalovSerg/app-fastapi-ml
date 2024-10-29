from fastapi import APIRouter


router = APIRouter(tags=["Auth User"])


@router.post("/get_token/")
def get_token():
    return {"message": "ok"}
