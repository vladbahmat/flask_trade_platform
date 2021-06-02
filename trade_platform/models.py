from flask_sqlalchemy import BaseQuery

from app import db
from flask_jwt_extended import create_access_token
from datetime import timedelta
from trade_platform.basic_model import BasicModel

class Currency(db.Model, BasicModel):
    __tablename__ = 'currency'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), unique=True)
    name = db.Column(db.String(20), unique=True)


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


class Profile(db.Model, BasicModel):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship("Currency")
    user = db.relationship("User", back_populates="profile")
    watchlist = db.relationship("WatchList", uselist=False, back_populates="profile")


items_watchlists = db.Table(
    'items_watchlists',
    db.Column('item_id', db.Integer(), db.ForeignKey('item.id')),
    db.Column('watchlist_id', db.Integer(), db.ForeignKey('watchlist.id'))
)


class Item(db.Model, BasicModel):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    code = db.Column(db.String(5), unique=True)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship("Currency")
    description = db.Column(db.String(100), default=" ")
    watchlists = db.relationship('WatchList', secondary=items_watchlists, backref=db.backref('items', lazy='dynamic'))


class WatchList(db.Model, BasicModel):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    profile = db.relationship("Profile", back_populates="watchlist")


class Inventory(db.Model, BasicModel):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    profile = db.relationship("Profile")
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = db.relationship("Item")
    quantity = db.Column(db.Integer, default=0)


class Offer(db.Model, BasicModel):
    __tablename__ = 'offer'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    profile = db.relationship("Profile")
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = db.relationship("Item")
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.DECIMAL, default=0, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    is_sell = db.Column(db.Boolean, default=True)


class Trade(db.Model, BasicModel):
    __tablename__ = 'trade'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = db.relationship("Item")
    seller_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    seller = db.relationship("Profile", foreign_keys=[seller_id])
    buyer_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    buyer = db.relationship("Profile", foreign_keys=[buyer_id])
    quantity = db.Column(db.Integer, default=0)
    description = db.Column(db.String(100), default=" ")
    seller_offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'), nullable=True)
    seller_offer = db.relationship("Offer", foreign_keys=[seller_offer_id])
    buyer_offer_id = db.Column(db.Integer, db.ForeignKey('offer.id'), nullable=True)
    buyer_offer = db.relationship("Offer", foreign_keys=[buyer_offer_id])

