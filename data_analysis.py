import pandas as pd
from sql_app.database import SessionLocal, engine
from sql_app import crud, schemas, models, database
from datetime import datetime

import os

db = SessionLocal()

def perform_analysis():
    stats = crud.get_stats(db)
    data = []
    for record in stats:
        payload = {
            "station": str(record[0]) if record[0] else None,
            "year": int(record[1]) if record[1] else None,
            "avg_max_temprature": round(record[2]/10 , 2) if record[2] else None,
            "avg_min_temprature": round(record[3]/10, 2) if record[3] else None,
            "sum_precipitation": int(record[4]) if record[4] else None
        }
        print(payload)
        data.append(schemas.Analysis.parse_obj(payload))
    crud.insert_analysis(db, data)
    print(f"records {len(stats)} is inserted.")


if __name__ == "__main__":
    perform_analysis()