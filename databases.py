import config
from sqlalchemy import create_engine, select, desc
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer


base = declarative_base()


class View(base):
    __tablename__ = "view"

    view_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    timezone = Column(String(50))
    ip = Column(String(100))


class Read(base):
    __tablename__ = "read"

    view_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    timezone = Column(String(50))
    ip = Column(String(100))


if __name__ == "__main__":
    engine = create_engine(config.DATABASE_URL)
    # base.metadata.create_all(engine)
    with engine.connect() as conn:
        command = select(Read.timestamp, Read.timezone, Read.ip).\
            order_by(desc("timestamp"))
        print(conn.execute(command).fetchall())

