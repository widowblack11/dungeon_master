from requests import Response, session
from dm_account_api.models.login_credentials import login_credentials


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)

    def post_v1_account_login(self, json: login_credentials, **kwargs) -> Response:
        """
        :param json login_credentials
        Authenticate via credentials
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/login",
            json=json,
            **kwargs
        )

        return response

    def delete_v1_account_login(self, **kwargs) -> Response:
        """"
        Logout as current user
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login",
            **kwargs
        )

        return response

    def delete_v1_account_delete(self, **kwargs) -> Response:
        """"
        Logout from every device
        :return:
        """

        response = self.session.delete(
            url=f"{self.host}/v1/account/login/all",
            **kwargs
        )

        return response
