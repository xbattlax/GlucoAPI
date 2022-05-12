import datetime
import json
from random import random
from time import sleep

import requests

if __name__ == '__main__':
    data = {
        "uuid": "da61fd19-c611-43f6-8c50-4b378b9e9d3e",
        "taux": "20",
        "created_at": "2022-05-04 09:00"
    }
    date = datetime.datetime.now() + datetime.timedelta(minutes=15)
    while True:
        randInt = random() * 100
        data["taux"] = str(randInt)
        date = date + datetime.timedelta(minutes=15)
        data["created_at"] = date.strftime("%Y-%m-%d %H:%M")
        headers = {'Content-Type': "application/json"}
        print(data)
        r = requests.post('http://52.47.108.118/add_glucose_record', data=json.dumps(data), headers=headers)
        print(r.json())
