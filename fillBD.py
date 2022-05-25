import datetime
import json
from random import random
from time import sleep

import requests

if __name__ == '__main__':
    data = {
        "uuid": "da61fd19-c611-43f6-8c50-4b378b9e9d3e",
        "hours_sleep": 20,
        "quality":1,
        "created_at": "2022-05-04 09:00"
    }
    date = datetime.datetime.now() + datetime.timedelta(minutes=15)
    while True:
        randInt = round(random() * 10)
        data["hours_sleep"] = randInt
        qualite = round(random() * 4)
        data["quality"] = qualite
        headers = {'Content-Type': "application/json"}
        print(data)

        date = date + datetime.timedelta(days=1)
        data["created_at"] = date.strftime("%Y-%m-%d %H:%M")
        headers = {'Content-Type': "application/json"}
        print(data)
        r = requests.post('http://127.0.0.1:8000/add_glucose_record', data=json.dumps(data), headers=headers)
        print(r.json())
