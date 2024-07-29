import requests


class HttpClient(object):
    def __init__(self, api_host, timeout=10):
        self.api_host = api_host
        self.timeout = timeout

    def request(
        self,
        url=None,
        method="",
        headers=None,
        cookies=None,
        verify=None,
        params=None,
        data=None,
        cert=None,
        auth=None,
        files=None,
        host=None,
    ):
        if host:
            api_host = host
        else:
            api_host = self.api_host
        url = api_host + url
        request_kwargs = dict(
            method=method,
            url=url,
            headers=headers,
            cookies=cookies,
            verify=verify,
            params=params,
            data=data,
            cert=cert,
            auth=auth,
            files=files,
        )

        try:
            response = requests.request(**request_kwargs)

        except requests.exceptions.ConnectionError as err_network:

            assert False, "Проблемы с сетью , ошибка %s" % err_network

        return response
