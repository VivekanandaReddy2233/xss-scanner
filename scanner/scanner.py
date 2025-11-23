"""Core scanning logic. Uses PayloadGenerator and RequestHandler.
It will try each parameter name, inject payloads for contexts and look for reflections.
It also attempts a simple HTML parse to classify where the token appeared (text, attr value, attr name, script).
"""
from .payload_generator import PayloadGenerator
from .request_handler import RequestHandler
from bs4 import BeautifulSoup

class Scanner:
    def __init__(self, base_url, params, method='GET', headers=None, cookies=None, contexts=None):
        self.base_url = base_url
        self.params = params or []
        self.method = method.upper()
        self.requester = RequestHandler(headers=headers, cookies=cookies)
        self.generator = PayloadGenerator()
        self.contexts = contexts or ['text', 'attr_value', 'attr_name']
        self.findings = []

    def _inject_into_params(self, param_name, payload):
        return {p: (payload if p == param_name else 'test') for p in self.params}

    def _detect_reflection(self, response_text, token):
        return token in response_text

    def _classify_context(self, html_text, token):
        """Try to classify where token appears in HTML.
        Returns one of: 'attr_name', 'attr_value', 'text', 'script', or 'unknown'
        """
        try:
            soup = BeautifulSoup(html_text, 'html.parser')
        except Exception:
            return 'unknown'

        # Check attribute names and values
        for tag in soup.find_all(True):
            for attr_name, attr_val in tag.attrs.items():
                if isinstance(attr_name, str) and token in attr_name:
                    return 'attr_name'
                if isinstance(attr_val, (str,)) and token in attr_val:
                    return 'attr_value'
                if isinstance(attr_val, (list, tuple)):
                    for v in attr_val:
                        if token in v:
                            return 'attr_value'

        # Check scripts
        for script in soup.find_all('script'):
            if script.string and token in script.string:
                return 'script'

        # Check visible text
        text = soup.get_text(separator=' ')
        if token in text:
            return 'text'

        return 'unknown'

    def run(self):
        token = self.generator.unique_token

        for p in self.params:
            for ctx in self.contexts:
                payloads = self.generator.get_payloads(ctx)
                for payload in payloads:
                    injected = self._inject_into_params(p, payload)

                    if self.method == 'GET':
                        r = self.requester.send_get(self.base_url, params=injected)
                    else:
                        r = self.requester.send_post(self.base_url, data=injected)

                    if r is None:
                        continue

                    body = r.text
                    if self._detect_reflection(body, token):
                        idx = body.find(token)
                        start = max(0, idx - 120)
                        end = min(len(body), idx + 120)
                        snippet = body[start:end]
                        detected_context = self._classify_context(body, token)

                        self.findings.append({
                            'param': p,
                            'context': detected_context or ctx,
                            'payload': payload,
                            'status_code': r.status_code,
                            'url': r.url,
                            'snippet': snippet
                        })

        return self.findings
