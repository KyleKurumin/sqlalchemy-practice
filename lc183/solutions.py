from sqlalchemy import func, distinct

from connection import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Customers, Orders


def lc183():
    session = Session(engine)

    subquery = session.query(1).filter(Customers.id == Orders.customerId)
    query = session.query(Customers.name).filter(~subquery.exists())
    print(query.all())


if __name__ == '__main__':
    lc183()
