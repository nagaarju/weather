from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from .database import Base


class Weather(Base):
    __tablename__ = "weather"

    station = Column(String)
    date = Column(Date)
    max_temprature = Column(Integer)
    min_temprature = Column(Integer)
    precipitation_amount = Column(Integer)
    __table_args__ = (
        PrimaryKeyConstraint(
            station,
            date),)

class Yield(Base):
    __tablename__ = "yield"

    year = Column(Integer, primary_key=True, index=True)
    grain_yield = Column(Integer)

class Analysis(Base):
    __tablename__ = "analysis"

    station = Column(String, primary_key = True)
    year = Column(Integer, primary_key = True)
    avg_min_temprature = Column(Float)
    avg_max_temprature = Column(Float)
    sum_precipitation = Column(Integer)