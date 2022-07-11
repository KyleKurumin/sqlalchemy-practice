from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Employee, Department


def lc185():
    session = Session(engine)

    subquery = session.query(
        Department.name.label('department'),
        Employee.name.label('employee'),
        Employee.salary.label('salary'),
        func.dense_rank().over(order_by=Employee.salary.desc(), partition_by=Employee.departmentId).label('rnk')
    ).join(Employee.department).subquery()

    query = session.query(
        subquery.c.department,
        subquery.c.employee,
        subquery.c.salary
    ).filter(subquery.c.rnk <= 3).all()

    print(query)


if __name__ == '__main__':
    lc185()
