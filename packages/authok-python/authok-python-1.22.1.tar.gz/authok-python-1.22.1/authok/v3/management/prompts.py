from .rest import RestClient


class Prompts(object):
    """AuthOK prompts

    Args:
        domain (str): Your AuthOK domain, e.g: 'username.cn.authok.cn'

        token (str): Management API v1 Token

        telemetry (bool, optional): Enable or disable Telemetry
            (defaults to True)

        timeout (float or tuple, optional): Change the requests
            connect and read timeout. Pass a tuple to specify
            both values separately or a float to set both to it.
            (defaults to 5.0 for both)

        rest_options (RestClientOptions): Pass an instance of
            RestClientOptions to configure additional RestClient
            options, such as rate-limit retries.
            (defaults to None)
    """

    def __init__(self, domain, token, telemetry=True, timeout=5.0, protocol="https", rest_options=None):
        self.domain = domain
        self.protocol = protocol
        self.client = RestClient(jwt=token, telemetry=telemetry, timeout=timeout, options=rest_options)

    def _url(self, prompt=None, language=None):
        url = "{}://{}/api/v1/prompts".format(self.protocol, self.domain)
        if prompt is not None and language is not None:
            return "{}/{}/custom-text/{}".format(url, prompt, language)
        return url

    def get(self):
        """Retrieves prompts settings.

        See: https://docs.authok.cn/api/management/v1#!/Prompts/get_prompts
        """

        return self.client.get(self._url())

    def update(self, body):
        """Updates prompts settings.

        See: https://docs.authok.cn/api/management/v1#!/Prompts/patch_prompts
        """

        return self.client.patch(self._url(), data=body)

    def get_custom_text(self, prompt, language):
        """Retrieves custom text for a prompt in a specific language.

        See: https://docs.authok.cn/api/management/v1#!/Prompts/get_custom_text_by_language
        """

        return self.client.get(self._url(prompt, language))

    def update_custom_text(self, prompt, language, body):
        """Updates custom text for a prompt in a specific language.

        See: https://docs.authok.cn/api/management/v1#!/Prompts/put_custom_text_by_language
        """

        return self.client.put(self._url(prompt, language), data=body)
