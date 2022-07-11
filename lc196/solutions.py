from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Person


def lc196():
    session = Session(engine)
    subquery = session.query(func.min(Person.id)).group_by(Person.email).subquery()
    session.query(Person).filter(Person.id.notin_(session.query(subquery))).delete(False)

    session.commit()


if __name__ == '__main__':
    lc196()
