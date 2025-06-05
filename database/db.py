from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.orm import (declarative_base, declared_attr, Session,
                            relationship)


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
    product_url = Column(String)
    img_url = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))


if __name__ == "__main__":
    engine = create_engine('sqlite:///sqlite.db', echo=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
