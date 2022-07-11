from datetime import date

from sqlalchemy import Date, Integer, Column
from sqlalchemy.orm import declarative_base, Session

from connection import engine

Base = declarative_base()


class Activity(Base):
    __tablename__ = 'lc511_activity'

    player_id = Column(Integer, primary_key=True)
    device_id = Column(Integer)
    event_date = Column(Date, primary_key=True)
    games_played = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        a1 = Activity(player_id=1, device_id=2, event_date=date(2016, 3, 1), games_played=5)
        a2 = Activity(player_id=1, device_id=2, event_date=date(2016, 5, 2), games_played=6)
        a3 = Activity(player_id=2, device_id=3, event_date=date(2017, 6, 25), games_played=1)
        a4 = Activity(player_id=3, device_id=1, event_date=date(2016, 3, 2), games_played=0)
        a5 = Activity(player_id=3, device_id=4, event_date=date(2018, 7, 3), games_played=5)

        session.add_all([a1, a2, a3, a4, a5])
        session.commit()
