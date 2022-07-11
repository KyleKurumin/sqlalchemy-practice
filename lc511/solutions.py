import datetime

from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Activity


def lc511():
    session = Session(engine)

    query = session.query(Activity.player_id, Activity.event_date.label('first_login')). \
        group_by(Activity.player_id).having(Activity.event_date == func.min(Activity.event_date))
    print(query.all())


if __name__ == '__main__':
    lc511()
