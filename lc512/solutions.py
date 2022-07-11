import datetime

from sqlalchemy import func, distinct, tuple_

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Activity


def lc512():
    session = Session(engine)

    subquery = session.query(Activity.player_id, func.min(Activity.event_date)). \
        group_by(Activity.player_id)

    query = session.query(Activity.player_id, Activity.device_id). \
        filter(tuple_(Activity.player_id, Activity.event_date).in_(subquery))

    print(query)


def lc512_v2():
    session = Session(engine)

    query = session.query(
        distinct(Activity.player_id),
        func.first_value(Activity.device_id).over(partition_by=Activity.player_id, order_by=Activity.event_date).label('device_id')
    )
    print(query.all())


if __name__ == '__main__':
    # lc512()
    lc512_v2()