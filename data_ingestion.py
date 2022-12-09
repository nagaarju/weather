import pandas as pd
from sql_app.database import SessionLocal, engine
from sql_app import crud, schemas, models, database
from datetime import datetime

import os

db = SessionLocal()
models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(bind=engine)

def insert_weather_file(df, station):
    total_count = len(df)
    data = []
    for row in df.itertuples(index=False):
        payload = {
            "station": station,
            "date": datetime.strptime(str(row.date), '%Y%m%d') if row.date != -9999 else None,
            "max_temprature": int(row.max_temprature) if row.max_temprature != -9999 else None,
            "min_temprature": int(row.min_temprature) if row.min_temprature != -9999 else None,
            "precipitation_amount": int(row.precipitation_amount) if row.precipitation_amount != -9999 else None
        }
        data.append(schemas.Weather.parse_obj(payload))
    crud.insert_weather(db, data)
    print(f"records {total_count} for station {station} is inserted.")

def weather_data_ingestion():
    directory = 'wx_data'
    for filename in os.listdir(directory):
        station = filename.split('.')[0]
        file = os.path.join(directory, filename)
        df = pd.read_csv(file, delimiter='\t', names=('date', 'max_temprature', 'min_temprature', 'precipitation_amount'))
        print(f"file {file} is being inserted.")
        insert_weather_file(df, station)


def insert_yield_file(df):
    total_count = len(df)
    data = []
    for row in df.itertuples(index=False):
        payload = {
            "year": int(row.year) if row.year != -9999 else None,
            "grain_yield": int(row.grain_yield) if row.grain_yield != -9999 else None
        }
        data.append(schemas.Yield.parse_obj(payload))
    crud.insert_yield(db, data)
    print(f"records {total_count} for yield is inserted.")

def yield_data_ingestion():
    directory = 'yld_data'
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        df = pd.read_csv(file, delimiter='\t', names=('year', 'grain_yield'))
        print(f"file {file} is being inserted.")
        insert_yield_file(df)

if __name__ == "__main__":
    weather_data_ingestion()
    yield_data_ingestion()