from datetime import timedelta

from flask_jwt_extended import create_access_token

from app import db
from trade_platform.models.basic_model import BasicModel


class User(db.Model, BasicModel):
    __tablename__  = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    profile = db.relationship("Profile", uselist=False, back_populates="user")

    def __init__(self, **kwargs):
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id,
            expires_delta=expire_delta
        )

        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email, cls.password == password).one()

        return user

