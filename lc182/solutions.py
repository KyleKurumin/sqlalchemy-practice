from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Person


def lc182():
    session = Session(engine)

    query = session.query(Person.email).group_by(Person.email).having(func.count() > 1).all()
    print(query)


if __name__ == '__main__':
    lc182()