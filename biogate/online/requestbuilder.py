import typing

import requests


class RequestBuilder(object):
    def __init__(self, base_url, **params):
        self.url = None
        self.params = None
        self.data = None
        self.headers = None
        self.cookies = None
        self.files = None
        self.auth = None
        self.timeout = None
        self.allow_redirects = None
        self.proxies = None
        self.hooks = None
        self.stream = None
        self.verify = None
        self.cert = None
        self.json = None

    def __getitem__(self, item) -> 'RequestBuilder':
        pass

    def __getattr__(self, item: str) -> 'RequestBuilder':
        pass

    def __call__(self, *args, **kwargs) -> 'RequestBuilder':
        pass

    def __truediv__(self, other: typing.Callable) -> requests.Response:
        pass

    def __rtruediv__(self, other: typing.Callable) -> requests.Response:
        return self / other
