from fastapi import APIRouter, Depends

from .schemas import UserSchema, TokenInfo, TokenSchema
from auth.utils import encode_jwt
from .dependencies import validate_token

router = APIRouter(tags=["ML Model"])


@router.get("/check/")
def get_status():
    return {"message": "ok"}


@router.post("/get-token/", response_model=TokenInfo)
def get_token(user: UserSchema):
    jwt_payload = {"sub": user.username, "tg_id": user.telegram_id}
    token = encode_jwt(jwt_payload)

    return TokenInfo(access_token=token)


@router.post("/model-response/")
def model_response(auth_user: UserSchema = Depends(validate_token)):
    return {"message": "Answer model", "user": auth_user}
