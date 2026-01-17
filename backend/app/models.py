
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base
import datetime

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    sku = Column(String, index=True, nullable=True)
    brand = Column(String, index=True)
    type = Column(String, index=True)
    size = Column(String, index=True)
    image = Column(String)
    entries = relationship('PriceEntry', back_populates='product')

class PriceEntry(Base):
    __tablename__ = 'price_entries'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    site = Column(String)
    price = Column(Float)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    meta = Column(JSON, nullable=True)
    product = relationship('Product', back_populates='entries')
