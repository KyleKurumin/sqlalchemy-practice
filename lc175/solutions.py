from connection import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Person, Address


def lc175():
    session = Session(engine)

    stmt = session.query(Person.lastName, Person.firstName, Address.city, Address.state).\
        outerjoin(Address, Person.personId == Address.personId)
    for item in stmt.all():
        print(item)


if __name__ == '__main__':
    lc175()
