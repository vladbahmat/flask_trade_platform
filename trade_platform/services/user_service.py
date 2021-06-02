from trade_platform.models import User

class UserService():

    @staticmethod
    def is_unique(email):
        if not User.query.filter_by(email=email).count():
            return True
