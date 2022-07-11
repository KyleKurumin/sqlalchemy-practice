import datetime

from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Weather


def lc197():
    session = Session(engine)

    w1 = aliased(Weather, name='w1')
    w2 = aliased(Weather, name='w2')

    query = session.query(w1.id).join(w2, func.datediff(w1.recordDate, w2.recordDate) == 1).filter(
        w1.temperature > w2.temperature)
    print(query.all())


if __name__ == '__main__':
    lc197()
