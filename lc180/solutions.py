from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Logs


def lc180():
    session = Session(engine)
    subquery = session.query(
        func.lag(Logs.num).over().label('prev'),
        Logs.num.label('current'),
        func.lead(Logs.num).over().label('post')
    ).subquery()

    query = session.query(distinct(subquery.c.current)).filter(subquery.c.prev == subquery.c.current,
                                                               subquery.c.current == subquery.c.post).all()

    print(query)


if __name__ == '__main__':
    lc180()
