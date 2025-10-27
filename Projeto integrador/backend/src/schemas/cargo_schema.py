from pydantic import BaseModel
from typing import Optional

class Cargo_create(BaseModel):
    id_empresa: int
    cargo: str

class Cargo_read(Cargo_create):
    id: int

    class Config:
        orm_mode = True

class Cargo_update(BaseModel):
    id: int
    id_empresa: Optional[int] = None
    cargo: Optional[str] = None
