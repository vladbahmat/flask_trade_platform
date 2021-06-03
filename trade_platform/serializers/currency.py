from pydantic import BaseModel


class CurrencySerializer(BaseModel):
    name:str
    code:str

    class Config:
        orm_mode = True


class CurrencyRetrieveSerializer(BaseModel):
    id:int
    name:str
    code:str

    class Config:
        orm_mode = True