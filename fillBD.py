import datetime
import json
import random
from time import sleep

import requests

if __name__ == '__main__':
    data = {
        "uuid": "da61fd19-c611-43f6-8c50-4b378b9e9d3e",
        "hours_sleep": 20,
        "quality":1,
        "date": "2022-05-04"
    }
    date = datetime.datetime.now() + datetime.timedelta(minutes=15)
    while True:
        randInt = random.randint(0, 9)
        data["hours_sleep"] = randInt
        qualite = random.randint(0, 4)
        data["quality"] = qualite
        headers = {'Content-Type': "application/json"}
        print(data)

        date = date + datetime.timedelta(days=1)
        data["date"] = date.strftime('%Y-%m-%d')
        headers = {'Content-Type': "application/json"}
        print(data)
        r = requests.post('http://127.0.0.1:8000/add_sleep_record', data=json.dumps(data), headers=headers)
        print(r.json())
