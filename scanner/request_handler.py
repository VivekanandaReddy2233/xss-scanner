import requests

class RequestHandler:
    def __init__(self, timeout=10, headers=None, cookies=None):
        self.timeout = timeout
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)
        if cookies:
            self.session.cookies.update(cookies)

    def send_get(self, url, params=None):
        try:
            r = self.session.get(url, params=params, timeout=self.timeout, allow_redirects=True)
            return r
        except Exception:
            return None

    def send_post(self, url, data=None, json=None):
        try:
            r = self.session.post(url, data=data, json=json, timeout=self.timeout, allow_redirects=True)
            return r
        except Exception:
            return None
