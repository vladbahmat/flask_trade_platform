from app import db
from trade_platform import BasicModel


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