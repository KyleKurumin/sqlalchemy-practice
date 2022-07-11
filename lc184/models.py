from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import Session, declarative_base, relationship

from connection import engine

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'lc184_employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))
    salary = Column(Integer, nullable=False)
    departmentId = Column(Integer, ForeignKey('lc184_department.id', ondelete='SET NULL'), nullable=True)

    department = relationship('Department', backref='employees')


class Department(Base):
    __tablename__ = 'lc184_department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        e1 = Employee(name='Joe', salary=70000, departmentId=1)
        e2 = Employee(name='Jim', salary=90000, departmentId=1)
        e3 = Employee(name='Henry', salary=80000, departmentId=2)
        e4 = Employee(name='Sam', salary=60000, departmentId=2)
        e5 = Employee(name='Max', salary=90000, departmentId=1)

        d1 = Department(name='IT')
        d2 = Department(name='Sales')

        session.add_all([d1, d2, e1, e2, e3, e4, e5])
        session.commit()
