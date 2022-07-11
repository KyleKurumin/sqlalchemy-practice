from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base, Session

from connection import engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'lc182_person'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        p1 = Person(email="a@b.com")
        p2 = Person(email="c@d.com")
        p3 = Person(email="a@b.com")

        session.add_all([p1, p2, p3])
        session.commit()
