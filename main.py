import requests
from datetime import datetime

APP_ID = "852e903a"
API_KEY = "d13f6a56a04e3d4e9c840e7b7c824911"

GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 183
AGE = 31

exercise_text = input("What exercise did you do good Sir?\n")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_data = {
     "query": exercise_text,
     "gender": GENDER,
     "weight_kg": WEIGHT_KG,
     "height_cm": HEIGHT_CM,
     "age": AGE
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_data)
response_data = response.json()["exercises"]

time_stamp = datetime.now()
date = time_stamp.strftime("%d/%m/%Y")
time = time_stamp.strftime("%X")

for task in range(len(response_data)):
    data = response_data[task]
    name = data["user_input"].title()
    duration = data["duration_min"]
    calories = data["nf_calories"]
    # Entering the data into google sheets using sheety
    sheety_endpoint = "https://api.sheety.co/198d9027ea41ea054b7525a9a3b7029b/kibirigeWorkouts/workouts"
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=body)
    print(sheety_response.text)




