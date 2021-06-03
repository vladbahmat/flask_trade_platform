from app import db
from trade_platform import BasicModel


class Inventory(db.Model, BasicModel):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    profile = db.relationship("Profile")
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = db.relationship("Item")
    quantity = db.Column(db.Integer, default=0)