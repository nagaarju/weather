from typing import List, Dict

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/weather/", response_model=Dict)
def read_weather(date: str = None, station: str = None, skip: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    weather = crud.get_weather(db, date=date, station=station, skip=skip, limit=limit)
    return {"skip": skip, "limit": limit, "data": list(weather)}

@app.get("/api/yield/", response_model=Dict)
def read_yield(year: int = None, skip: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    yield_data = crud.get_yield(db, year=year, skip=skip, limit=limit)
    return {"skip": skip, "limit": limit, "data": list(yield_data)}

@app.get("/api/weather/stats", response_model=Dict)
def read_analysis(year: int = None, station: str = None, skip: int = 0, limit: int = 25, db: Session = Depends(get_db)):
    analysis = crud.get_analysis(db, year=year, station=station, skip=skip, limit=limit)
    return {"skip": skip, "limit": limit, "data": list(analysis)}