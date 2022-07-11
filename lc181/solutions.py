from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Employee


def lc181():
    session = Session(engine)
    al = aliased(Employee)
    query = session.query(Employee.name).join(Employee.manager.of_type(al)).filter(Employee.salary > al.salary)

    print(query.all())


if __name__ == '__main__':
    lc181()
