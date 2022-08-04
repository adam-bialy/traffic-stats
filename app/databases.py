import hashlib


from sqlalchemy import Column, String, DateTime, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class View(db.Model):
    __tablename__ = "view"

    view_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    timezone = Column(String(50))


class Read(db.Model):
    __tablename__ = "read"

    read_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    timezone = Column(String(50))


class User(UserMixin, db.Model):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)


def hash_password(password):
    return hashlib.sha256((password+"2137").encode()).hexdigest()

