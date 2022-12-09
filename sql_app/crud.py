from sqlalchemy.orm import Session
from sqlalchemy import func, and_, Date
from typing import List
from datetime import datetime

from . import models, schemas

def insert_weather(db: Session, weathers: List[schemas.Weather]):
    weathers = [models.Weather(**weather.dict()) for weather in weathers]
    db.bulk_save_objects(weathers)
    db.commit()

def insert_yield(db: Session, yield_vars: schemas.Yield):
    yield_vars = [models.Yield(**yield_var.dict()) for yield_var in yield_vars]
    db.bulk_save_objects(yield_vars)
    db.commit()

def insert_analysis(db: Session, analysis: schemas.Analysis):
    analysis = [models.Analysis(**stat.dict()) for stat in analysis]
    db.bulk_save_objects(analysis)
    db.commit()

def get_stats(db: Session):
    return db.query(models.Weather.station,func.strftime('%Y',models.Weather.date), func.avg(models.Weather.max_temprature), func.avg(models.Weather.min_temprature), func.sum(models.Weather.precipitation_amount)).group_by(models.Weather.station, func.strftime('%Y',models.Weather.date)).all()

def get_weather(db: Session, date: str = None, station: str = None, skip: int = 0, limit: int = 100):
    result= db.query(models.Weather)
    if date:
        try:
            datetime.strptime(str(date), '%Y-%m-%d')
        except:
            return [{"error": "please provide the date in YYYY-MM-DD format."}]
        result = result.filter(models.Weather.date == date)
    if station:
        result = result.filter(models.Weather.station == station)
    return result.offset(skip).limit(limit).all()

def get_yield(db: Session, year: int = None, skip: int = 0, limit: int = 100):
    result = db.query(models.Yield)
    if year:
        result = result.filter(models.Yield.year == year)
    return result.offset(skip).limit(limit).all()

def get_analysis(db: Session, year: int = None, station: str = None, skip: int = 0, limit: int = 100):
    result = db.query(models.Analysis)
    if year:
        result = result.filter(models.Analysis.year == year)
    if station:
        result = result.filter(models.Analysis.station == station)

    return result.offset(skip).limit(limit).all()