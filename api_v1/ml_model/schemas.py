from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    telegram_id: int


class TokenSchema(BaseModel):
    access_token: str


class TokenInfo(TokenSchema):
    token_type: str = "Bearer"
