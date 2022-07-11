from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship

from connection import engine

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'lc185_employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    salary = Column(Integer, nullable=False)
    departmentId = Column(Integer, ForeignKey('lc185_department.id', ondelete='SET NULL'), nullable=True)

    department = relationship('Department', backref='employees')


class Department(Base):
    __tablename__ = 'lc185_department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        d1 = Department(name='IT')
        d2 = Department(name='Sales')

        e1 = Employee(name='Joe', salary=85000, departmentId=1)
        e2 = Employee(name='Henry', salary=80000, departmentId=2)
        e3 = Employee(name='Sam', salary=60000, departmentId=2)
        e4 = Employee(name='Max', salary=90000, departmentId=1)
        e5 = Employee(name='Janet', salary=69000, departmentId=1)
        e6 = Employee(name='Randy', salary=85000, departmentId=1)
        e7 = Employee(name='Will', salary=70000, departmentId=1)

        session.add_all([d1, d2, e1, e2, e3, e4, e5, e6, e7])
        session.commit()