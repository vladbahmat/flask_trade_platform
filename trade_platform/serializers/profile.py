from pydantic import BaseModel

from trade_platform.serializers.currency import CurrencySerializer
from trade_platform.serializers.user import UserSerializer


class ProfileSerializer(BaseModel):
    id:int
    user: UserSerializer
    currency: CurrencySerializer

    class Config:
        orm_mode = True