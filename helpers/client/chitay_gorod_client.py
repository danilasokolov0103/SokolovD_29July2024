import json

import allure
import curlify
import requests
from allure_commons.types import AttachmentType as AT

from config import config
from helpers.client.http_client import HttpClient


def get_token():
    response = requests.get(config.get('BASE_URL'))
    set_cookie_header = response.headers.get('Set-Cookie')
    token = set_cookie_header.split('Bearer%20')[1].split(';')[0]
    return token


class ChitayGorodClient(object):
    def __init__(self):
        self.API_HOST = config.get("BASE_API_URL")
        self.token = get_token()
        self.headers = {
            "Authorization": "Bearer %s" % self.token,
            "Content-Type": "application/json",
        }
        self._http_client = HttpClient(api_host=self.API_HOST)
        self.auth = None

    def base_api(
            self,
            method,
            url=None,
            data=None,
            params=None,
            headers=None,
            cookies=None,
            files=None,
            cert=None,
            auth=None,
            verify=False,
            host=None,
            json_dumps=True,
            add_curl=True,
    ):
        if headers is False:
            request_headers = {}
        else:
            request_headers = self.headers
        if data and json_dumps:
            data = json.dumps(data, ensure_ascii=False).encode("utf-8")
            allure.attach(data, "Отправляемые в запрос данные", AT.JSON)
        response = self._http_client.request(
            method=method,
            url=url,
            data=data,
            headers=request_headers,
            params=params,
            cert=cert,
            cookies=cookies,
            auth=auth,
            files=files,
            verify=verify,
            host=host,
        )
        if add_curl:
            request_curl_attach(response.request)
        return response


def request_curl_attach(response):
    allure.attach(curlify.to_curl(response), "CURL", AT.TEXT)


chitay_gorod_client = ChitayGorodClient()
