from app import db
from trade_platform.models.basic_model import BasicModel


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