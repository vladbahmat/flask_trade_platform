from trade_platform.models import Currency, User, Profile

class ProfileService():
    @staticmethod
    def profile_autocreate(user):
        data = {"user":user}
        Profile(**data).insert()