import requests
from requests.exceptions import HTTPError

from config import REBOT_API, REBOT_TOKEN

DEFAULT_TIMEOUT_SECONDS = 10


class RebotClient(requests.Session):
    def __init__(self, base_url=REBOT_API, timeout=DEFAULT_TIMEOUT_SECONDS):
        super(RebotClient, self).__init__()
        self.base_url = base_url
        self._timeout = timeout
        self._headers = {"Content-Type": "application/json"}
        self.mount('https://', requests.adapters.HTTPAdapter(max_retries=3))

    def _set_request_timeout(self, kwargs):
        kwargs.setdefault('timeout', self._timeout)
        kwargs.setdefault('headers', self._headers)
        return kwargs

    def _url(self, path):
        return '{0}{1}'.format(self.base_url, path)

    def _post(self, url, **kwargs):
        return self.post(url, **self._set_request_timeout(kwargs))

    def _patch(self, url, **kwargs):
        return self.patch(url, **self._set_request_timeout(kwargs))

    def _get(self, url, **kwargs):
        return self.get(url, **self._set_request_timeout(kwargs))

    def _put(self, url, **kwargs):
        return self.put(url, **self._set_request_timeout(kwargs))

    def _delete(self, url, **kwargs):
        return self.delete(url, **self._set_request_timeout(kwargs))

    def _head(self, url, **kwargs):
        return self.head(url, **self._set_request_timeout(kwargs))

    @staticmethod
    def _result(response):
        try:
            response.raise_for_status()
        except HTTPError:
            raise
        body = response.json()
        return body.get("text", "Sorry, I don't know what can I do.")

    def get_message(self, user_id, message):
        data = {
            "key": REBOT_TOKEN,
            "info": message,
            "userid": user_id,
        }
        try:
            message = self._result(self._post(self._url("/api"), json=data))
        except HTTPError as e:
            print(e)
            return "Sorry, Something Wrong."
        return message
