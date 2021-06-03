from app import db
from trade_platform import BasicModel


class Currency(db.Model, BasicModel):
    __tablename__ = 'currency'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), unique=True)
    name = db.Column(db.String(20), unique=True)