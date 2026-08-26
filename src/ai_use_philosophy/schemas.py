# schemas.py
from pydantic import BaseModel


class PrincipleOut(BaseModel):
    id: int
    principle: str
