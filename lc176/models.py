from connection import engine

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'lc176_employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    salary = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        e1 = Employee(salary=100)
        e2 = Employee(salary=200)
        e3 = Employee(salary=300)

        session.add_all([e1, e2, e3])
        session.commit()
