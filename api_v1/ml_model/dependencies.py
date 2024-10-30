from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException, status
from auth.utils import decode_jwt
from .schemas import TokenSchema, UserSchema


def validate_token(token: TokenSchema) -> UserSchema:
    try:
        payload = decode_jwt(token.access_token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalide token"
        )

    user = UserSchema(username=payload.get("sub"), telegram_id=payload.get("tg_id"))

    return user
