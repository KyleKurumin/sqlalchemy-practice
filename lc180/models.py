from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, Session

from connection import engine

Base = declarative_base()


class Logs(Base):
    __tablename__ = 'lc180_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    num = Column(Integer, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        l1 = Logs(num=1)
        l2 = Logs(num=1)
        l3 = Logs(num=1)
        l4 = Logs(num=2)
        l5 = Logs(num=1)
        l6 = Logs(num=2)
        l7 = Logs(num=2)

        session.add_all([l1, l2, l3, l4, l5, l6, l7])
        session.commit()