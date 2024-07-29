import json

import allure
from allure_commons.types import AttachmentType as AT


def attach_data(data, attach_name, requests_response=True):
    if requests_response:
        data = data.json()
    allure.attach(json.dumps(data, ensure_ascii=False), attach_name, AT.JSON)
