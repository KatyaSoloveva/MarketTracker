from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, declared_attr, relationship


class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class User(Base):
    user_id = Column(Integer, unique=True)
    username = Column(String)
    products = relationship("Product", backref="user")


class Product(Base):
    shop = Column(String)
    title = Column(String)
    price = Column(Integer)
    desired_price = Column(Integer)
    product_url = Column(String)
    article_number = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
