import datetime

from sqlalchemy import func, distinct, tuple_, and_
from sqlalchemy.sql.expression import text

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Employee


def lc570():
    session = Session(engine)

    e1 = aliased(Employee, name='e1')
    e2 = aliased(Employee, name='e2')

    query = session.query(distinct(e2.name)).\
        select_from(e1).\
        join(e2, e1.managerId == e2.id).\
        group_by(e2.id).having(func.count(e2.id) >= 5)

    print(query)


if __name__ == '__main__':
    lc570()
