from app import db
from trade_platform import BasicModel


class WatchList(db.Model, BasicModel):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    profile = db.relationship("Profile", back_populates="watchlist")