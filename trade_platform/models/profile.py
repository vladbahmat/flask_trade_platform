from app import db
from trade_platform import BasicModel


class Profile(db.Model, BasicModel):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))
    currency = db.relationship("Currency")
    user = db.relationship("User", back_populates="profile")
    watchlist = db.relationship("WatchList", uselist=False, back_populates="profile")