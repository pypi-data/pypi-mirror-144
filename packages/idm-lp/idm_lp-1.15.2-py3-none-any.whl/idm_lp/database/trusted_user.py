from pydantic import BaseModel


class TrustedUser(BaseModel):
    user_id: int

