from connection import engine

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class Person(Base):
    __tablename__ = "lc175_person"

    personId = Column(Integer, primary_key=True, autoincrement=True)
    lastName = Column(String(30))
    firstName = Column(String(30))

    def __str__(self):
        return f'{self.personId}, {self.lastName}, {self.firstName}'


class Address(Base):
    __tablename__ = "lc175_address"

    addressId = Column(Integer, primary_key=True, autoincrement=True)
    personId = Column(Integer)
    city = Column(String(30))
    state = Column(String(30))

    def __str__(self):
        return f'{self.addressId}, {self.city}, {self.state}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        p1 = Person(lastName='Wang', firstName='Allen')
        p2 = Person(lastName='Alice', firstName='Bob')

        a1 = Address(personId=2, city='New York City', state='NewYork')
        a2 = Address(personId=3, city='Leetcode', state='California')

        session.add_all([p1, p2, a1, a2])
        session.commit()

