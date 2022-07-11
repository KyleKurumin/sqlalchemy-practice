from sqlalchemy import Integer, String, Column, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import declarative_base, Session, relationship, backref

from connection import engine

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'lc181_employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    salary = Column(Integer)
    managerId = Column(Integer, ForeignKey('lc181_employee.id'), nullable=True)

    manager = relationship('Employee', remote_side=[id], backref='subordinate')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        e1 = Employee(id=1, name='Joe', salary=70000, managerId=3)
        e2 = Employee(id=2, name='Henry', salary=80000, managerId=4)
        e3 = Employee(id=3, name='Sam', salary=80000, managerId=None)
        e4 = Employee(id=4, name='Max', salary=90000, managerId=None)

        session.add_all([e3, e4, e1, e2])
        session.commit()
