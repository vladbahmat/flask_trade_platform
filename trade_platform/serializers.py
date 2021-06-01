from pydantic import BaseModel

class UserSerializer(BaseModel):
    username:str
    email:str
    password:str

    class Config:
        orm_mode = True


class CurrencySerializer(BaseModel):
    name:str
    code:str

    class Config:
        orm_mode = True
