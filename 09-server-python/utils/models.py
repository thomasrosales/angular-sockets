from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from settings.database import Base
import datetime


class BaseMixin(object):

    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, default=True, nullable=False)


class DateAware(BaseMixin, Base):
    __abstract__ = True

    created = Column(DateTime, default=datetime.datetime.today())
    modified = Column(DateTime, default=datetime.datetime.today())


class Image(DateAware):
    __abstract__ = True

    path = Column(String(100), unique=True, nullable=False)
