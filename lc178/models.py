from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Numeric, Integer, Column
from connection import engine

Base = declarative_base()


class Scores(Base):
    __tablename__ = 'lc178_scores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Numeric(5, 2))


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        s1 = Scores(score=3.5)
        s2 = Scores(score=3.65)
        s3 = Scores(score=4.)
        s4 = Scores(score=3.85)
        s5 = Scores(score=4.)
        s6 = Scores(score=3.65)

        session.add_all([s1, s2, s3, s4, s5, s6])
        session.commit()
