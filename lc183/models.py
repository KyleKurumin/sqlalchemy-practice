from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship

from connection import engine

Base = declarative_base()


class Customers(Base):
    __tablename__ = 'lc183_customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class Orders(Base):
    __tablename__ = 'lc183_orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customerId = Column(Integer, ForeignKey('lc183_customers.id', ondelete='CASCADE'))

    customer = relationship('Customers', backref='orders')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        c1 = Customers(name='Joe')
        c2 = Customers(name='Henry')
        c3 = Customers(name='Sam')
        c4 = Customers(name='Max')

        o1 = Orders(customerId=3)
        o2 = Orders(customerId=1)

        session.add_all([c1, c2, c3, c4, o1, o2])
        session.commit()
