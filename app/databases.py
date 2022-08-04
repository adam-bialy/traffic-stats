import app.config as config
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, DateTime, Integer


base = declarative_base()


class View(base):
    __tablename__ = "view"

    view_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    timezone = Column(String(50))


class Read(base):
    __tablename__ = "read"

    read_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    timezone = Column(String(50))


class User(base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)


def create_tables(engine):
    base.metadata.create_all(engine)


def clear_tables(engine):
    with Session(engine) as session:
        session.query(View).delete()
        session.query(Read).delete()
        session.commit()


if __name__ == "__main__":
    engine = create_engine(config.DATABASE_URL)
    clear_tables(engine)
