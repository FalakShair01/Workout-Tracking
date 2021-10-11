import requests
from datetime import datetime
import os

GENDER = "male"
HEIGHT_CM = 161
WEIGHT_KG = 42
AGE = 19


APP_ID = os.environ.get("YOUR_APP_ID")
API_KEY = os.environ.get("YOUR_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("YOUR_WORKSHEET_ENDPOINT")

exercise_text = input("Tell as which exercise you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%x")
time_now = datetime.now().strftime("%X")

for exercise in result['exercises']:

    sheet_inputs = {

        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],

        }
    }

    headers = {
        "Authorization": os.environ.get("Bearer YOUR_KEY")
    }

    response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=headers)