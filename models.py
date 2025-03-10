from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    surname: Optional[str]
    phone: str
    message: str
    is_admin: bool