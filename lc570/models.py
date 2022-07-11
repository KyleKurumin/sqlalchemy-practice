from datetime import date

from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship, backref

from connection import engine

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'lc570_employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    department = Column(String(30))
    managerId = Column(Integer, ForeignKey('lc570_employee.id'))

    manager = relationship('Employee', backref=backref('subordinates', remote_side=[id]))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        e1 = Employee(id=101, name='John', department='A')
        e2 = Employee(id=102, name='Dan', department='A', managerId=101)
        e3 = Employee(id=103, name='James', department='A', managerId=101)
        e4 = Employee(id=104, name='Amy', department='A', managerId=101)
        e5 = Employee(id=105, name='Anne', department='A', managerId=101)
        e6 = Employee(id=106, name='Ron', department='B', managerId=101)

        session.add_all([e1, e2, e3, e4, e5, e6])
        session.commit()