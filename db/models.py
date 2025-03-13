from connection import Base
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey

class ProductTypeModel(Base):
    __tablename__ = "product_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    coef = Column(Float, nullable=False)

class MaterialTypeModel(Base):
    __tablename__ = "material_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    coef = Column(Float, nullable=False)

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    article = Column(String, nullable=False)
    min_cost = Column(Float, nullable=False)

    product_type = Column(Integer, ForeignKey('product_types.id'), nullable=False)

class PartnerModel(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    boss_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    inn = Column(String, nullable=False)
    rate = Column(Integer, nullable=False)

class OrderModel(Base):
    __tablename__ = "orders"

    product = Column(Integer, ForeignKey('products.id'), primary_key=True)
    partner = Column(Integer, ForeignKey('partners.id'), primary_key=True)
    count = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
