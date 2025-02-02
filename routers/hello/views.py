import logging

import requests

from depends.settings import BASE_URL, ARTIFACT_TOKEN


def move(x: int, y: int):
    url = BASE_URL + "/action/move"
    data = {
        "x": x,
        "y": y,
    }
    headers = {
        'Content-Type': 'application/json',
        "Accept": 'application/json',
        "Authorization": 'Bearer ' + ARTIFACT_TOKEN
    }
    response = requests.post(url, json=data, headers=headers)
    logging.debug(response.status_code)
    logging.debug(response.content)