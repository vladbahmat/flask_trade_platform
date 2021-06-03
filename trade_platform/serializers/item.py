from typing import Optional

from pydantic import BaseModel


class ItemSerializer(BaseModel):
    name: str
    code: str
    currency_id: int
    description: Optional[str]

    class Config:
        orm_mode = True