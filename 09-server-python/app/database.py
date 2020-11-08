import pymysql
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ
from flask import current_app


CONFIG = current_app.config
database = CONFIG["SQLALCHEMY_URL"]


engine = create_engine(database, convert_unicode=False)

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = Session.query_property()


def init_db():
    # import all modules here that might define models so that
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)
