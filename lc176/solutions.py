from sqlalchemy import func

from connection import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Employee


def lc176():
    session = Session(engine)

    subquery = session.query(
        Employee.id.label('id'),
        Employee.salary.label('salary'),
        func.dense_rank().over(order_by=Employee.salary.desc()).label('rnk')
    ).subquery()

    query = session.query(subquery.c.id, subquery.c.salary).filter(
        subquery.c.rnk == 2
    ).one()

    print(query)


if __name__ == '__main__':
    lc176()