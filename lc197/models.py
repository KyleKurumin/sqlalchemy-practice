from sqlalchemy import Date, Integer, Column
from sqlalchemy.orm import Session, declarative_base

from connection import engine

import datetime

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'lc197_weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    recordDate = Column(Date)
    temperature = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        w1 = Weather(recordDate=datetime.date(2015, 1, 1), temperature=10)
        w2 = Weather(recordDate=datetime.date(2015, 1, 2), temperature=25)
        w3 = Weather(recordDate=datetime.date(2015, 1, 3), temperature=20)
        w4 = Weather(recordDate=datetime.date(2015, 1, 4), temperature=30)

        session.add_all([w1, w2, w3, w4])
        session.commit()
