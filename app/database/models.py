from config import db


class Orders(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer)
    price_usd = db.Column(db.Float)
    price_rub = db.Column(db.Float)
    delivery_time = db.Column(db.Date)

    def __repr__(self):
        return f'Order: {self.order}, USD: {self.price_usd}, RUB: {self.price_rub}, Delivery: {self.delivery_time}, '
