from datetime import date

from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship, backref

from connection import engine

Base = declarative_base()


class Candidate(Base):
    __tablename__ = 'lc574_candidate'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    votes = relationship('Vote', back_populates='candidate')


class Vote(Base):
    __tablename__ = 'lc574_vote'

    id = Column(Integer, primary_key=True)
    candidateId = Column(Integer, ForeignKey('lc574_candidate.id'))

    candidate = relationship('Candidate', back_populates='votes')


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        c1 = Candidate(id=1, name='A')
        c2 = Candidate(id=2, name='B')
        c3 = Candidate(id=3, name='C')
        c4 = Candidate(id=4, name='D')
        c5 = Candidate(id=5, name='E')

        v1 = Vote(id=1, candidateId=2)
        v2 = Vote(id=2, candidateId=4)
        v3 = Vote(id=3, candidateId=3)
        v4 = Vote(id=4, candidateId=2)
        v5 = Vote(id=5, candidateId=5)
        v6 = Vote(id=6, candidateId=3)
        v7 = Vote(id=7, candidateId=3)

        session.add_all([c1, c2, c3, c4, c5, v1, v2, v3, v4, v5, v6, v7])

        session.commit()