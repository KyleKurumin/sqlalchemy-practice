import datetime

from sqlalchemy import func, distinct, tuple_, and_
from sqlalchemy.sql.expression import text

from connection import engine
from sqlalchemy.orm import Session, aliased
from sqlalchemy import select

from models import Candidate, Vote


def lc154():
    session = Session(engine)

    subquery = session.query(Vote.candidateId).group_by(Vote.candidateId).order_by(
        func.count(Vote.candidateId).desc()).limit(
        1).scalar_subquery()

    query = session.query(Candidate.name).filter(Candidate.id == subquery)

    print(query.all())


if __name__ == '__main__':
    lc154()
