from sqlalchemy import func

from connection import engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import Scores


def lc178():
    session = Session(engine)

    query = session.query(
        Scores.score.label('score'),
        func.dense_rank().over(
            order_by=Scores.score.desc()
        )
    ).all()

    print(query)


if __name__ == '__main__':
    lc178()
    