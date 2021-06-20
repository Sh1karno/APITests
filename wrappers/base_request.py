import requests


class BaseRequest:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, url: str = '', params=None):
        return requests.get(self.base_url + url, params=params)

    def post(self, url, data):
        return requests.post(self.base_url + url, data)

    def put(self, url, data):
        return requests.put(self.base_url + url, data)
