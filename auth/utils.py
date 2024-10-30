from datetime import datetime, timedelta, timezone
import jwt
import bcrypt

from core.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
):
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        iat=now,
        exp=expire,
    )
    encode = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encode


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
):
    decode = jwt.decode(token, public_key, algorithms=[algorithm])
    return decode
