from app import db
from trade_platform.models.basic_model import BasicModel


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