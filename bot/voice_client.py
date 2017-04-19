import requests
from requests.exceptions import HTTPError

from config import VOICE_API, VOICE_TOKEN, VOICE_ADMIN_ID

DEFAULT_TIMEOUT_SECONDS = 10


class VoiceClient(requests.Session):
    def __init__(self, base_url=VOICE_API, timeout=DEFAULT_TIMEOUT_SECONDS):
        super(VoiceClient, self).__init__()
        self.base_url = base_url
        self._timeout = timeout
        self._headers = {"Content-Type": "application/json"}
        self._headers.update(
            dict(Authorization="token {}".format(VOICE_TOKEN))
        )
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

    def send_message_to_user(self, conversation_id, message):
        data = {
            "admin": {
                "admin_id": VOICE_ADMIN_ID,
            },
            "message_type": "comment",
            "body": message,
        }
        try:
            url = "/v1/conversations/{conversation_id}/reply".format(conversation_id=conversation_id)
            self._result(self._post(self._url(url), json=data))
        except HTTPError as e:
            print(e)
            return False
        return True

