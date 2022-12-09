from sys import api_version
import unittest
from fastapi.testclient import TestClient
from sql_app import crud, database, models, schemas
from sql_app.main import app

client = TestClient(app)

class TestAll(unittest.TestCase):

    def test_get_weather(self):
        mock_data = [{"station":"USC00254440","max_temprature":28,"precipitation_amount":3,"min_temprature":-128,"date":"1985-01-01"}]
        params = {"date": "1985-01-01",
                  "station" : "USC00254440"
            }
        response = client.get("/api/weather", params = params)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('data'), mock_data)

    def test_get_yield(self):
        mock_data = [{"year":1985,"grain_yield":225447}]
        params = {"year": 1985,
            }
        response = client.get("/api/yield/", params = params)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('data'), mock_data)

    def test_get_stats(self):
        mock_data = [{"avg_max_temprature":19.27,"station":"USC00110187","avg_min_temprature":7.81,"sum_precipitation":14655,"year":1985}]
        params = {"year": 1985,
                "station" : "USC00110187"
            }
        response = client.get("/api/weather/stats/", params = params)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('data'), mock_data)