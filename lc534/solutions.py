import datetime

from sqlalchemy import func, distinct, tuple_, and_

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Activity


def lc534():
    session = Session(engine)

    a1 = aliased(Activity, name='a1')
    a2 = aliased(Activity, name='a2')

    p = session.query(a1.player_id, a1.event_date, func.sum(a2.games_played)). \
        select_from(a1). \
        join(a2, and_(a1.player_id == a2.player_id, a2.event_date <= a1.event_date)).\
        group_by(a1.player_id, a1.event_date)

    print(p.all())


def lc534_v2():
    session = Session(engine)

    query = session.query(
        Activity.player_id,
        Activity.event_date,
        func.sum(Activity.games_played).over(partition_by=Activity.player_id, order_by=Activity.event_date).label(
            'game_played')
    )
    print(query.all())


if __name__ == '__main__':
    lc534()
    # lc534_v2()
