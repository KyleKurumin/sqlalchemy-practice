import datetime

from sqlalchemy import func, distinct, tuple_, and_
from sqlalchemy.sql.expression import text

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Activity


def lc550():
    session = Session(engine)

    distinct_count = session.query(func.count(distinct(Activity.player_id))).scalar_subquery()

    subquery = session.query(
        Activity.player_id.label('player_id'),
        Activity.event_date.label('event_date'),
        func.lag(Activity.event_date).over(partition_by=Activity.player_id, order_by=Activity.event_date).label('prev'),
        func.lead(Activity.event_date).over(partition_by=Activity.player_id, order_by=Activity.event_date).label('post')
    ).subquery()

    query = session.query(
        func.count(distinct(subquery.c.player_id)) / distinct_count
    ). \
        select_from(subquery). \
        filter(subquery.c.prev == None, func.datediff(subquery.c.post, subquery.c.event_date) == 1)

    print(query.all())


def lc550_v2():
    session = Session(engine)

    subquery = session.query(
        Activity.player_id,
        func.date_add(func.min(Activity.event_date), text('interval 1 day'))
    ).group_by(Activity.player_id)

    distinct_count = session.query(func.count(distinct(Activity.player_id))).scalar_subquery()

    query = session.query(
        func.round(func.count(distinct(Activity.player_id)) / distinct_count, 2).label('fraction')
    ).filter(tuple_(Activity.player_id, Activity.event_date).in_(subquery))

    print(query.all())


if __name__ == '__main__':
    lc550_v2()
