from sqlalchemy import Column, BIGINT, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Orders(Base):
    __tablename__ = 'Orders'
    id = Column(BIGINT, primary_key=True)
    order = Column(BIGINT)
    price_usd = Column(Float)
    price_rub = Column(Float)
    delivery_time = Column(Date)

    def __repr__(self):
        return f'Order: {self.order}, USD: {self.price_usd}, RUB: {self.price_rub}, Delivery: {self.delivery_time}, '
