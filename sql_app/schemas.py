from typing import List, Union, Optional
from datetime import date

from pydantic import BaseModel


class Weather(BaseModel):
    station: str
    date: date
    max_temprature: Optional[int] = None 
    min_temprature: Optional[int] = None
    precipitation_amount: Optional[int] = None

    class Config:
        orm_mode = True

class Yield(BaseModel):
    year: int
    grain_yield: Optional[int] = None

    class Config:
        orm_mode = True

class Analysis(BaseModel):
    station: str
    year: int
    avg_min_temprature: Optional[float] = None
    avg_max_temprature: Optional[float] = None
    sum_precipitation: Optional[int] = None

    class Config:
        orm_mode = True