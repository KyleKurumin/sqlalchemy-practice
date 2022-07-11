from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Employee, Department


def lc184():
    session = Session(engine)

    included = session.query(Department.name.label('department'),
                             Employee.name.label('employee'),
                             Employee.salary.label('salary'),
                             func.dense_rank().over(order_by=Employee.salary.desc(),
                                                    partition_by=Employee.departmentId).label('rnk')
                             ).join(Employee.department).subquery()
    query = session.query(included.c.department, included.c.employee, included.c.salary).filter(
        included.c.rnk == 1).all()
    print(query)


if __name__ == '__main__':
    lc184()
