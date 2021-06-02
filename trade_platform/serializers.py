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


class CurrencyRetrieveSerializer(BaseModel):
    id:int
    name:str
    code:str

    class Config:
        orm_mode = True


class ProfileSerializer(BaseModel):
    id:int
    user: UserSerializer
    currency: CurrencySerializer

    class Config:
        orm_mode = True

