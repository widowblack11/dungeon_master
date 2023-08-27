from requests import Response, session
from dm_account_api.models.login_credentials import LoginCredentialsModel
from dm_account_api.models.user_envelope import UserEnvelope
from restclient.restclient import Restclient


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentialsModel, **kwargs) -> Response:
        """
        :param json login_credentials
        Authenticate via credentials
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/login",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def delete_v1_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login",
            **kwargs
        )

        return response

    def delete_v1_account_delete(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """

        response = self.client.delete(
            path=f"/v1/account/login/all",
            **kwargs
        )

        return response
