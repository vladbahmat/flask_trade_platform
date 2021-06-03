from trade_platform.models import Profile

class ProfileService():
    @staticmethod
    def profile_autocreate(user):
        data = {"user":user}
        profile = Profile(**data).insert()

        return profile