import token

from requests import Response
from dm_account_api.models.registration_model import registration_model
from dm_account_api.models.reset_password import reset_password
from dm_account_api.models.change_email import change_email
from dm_account_api.models.change_password import change_password
from requests import session


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account",
            json=json,
            **kwargs
        )

        return response

    def post_v1_account_password(self, json: reset_password, **kwargs) -> Response:
        """
        :param json reset_password
        Reset registered user password
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_email(self, json: change_email, **kwargs) -> Response:
        """
        :param json change_email
        Change registered user email
        :return:
        """

        response = self.session.post(
            url=f"{self.host}/v1/account/email",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_password(self, json: change_password, **kwargs) -> Response:
        """
        :param json change_password
        Change registered user password
        :return:
        """

        response = self.session.put(
            url=f"{self.host}/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_token(self, **kwargs) -> Response:
        """
        Activate registered user
        :return:
        """

        token = '8384d440-c461-4e31-b032-74b0dbfa7980'

        response = self.session.put(
            url=f'{self.host}/v1/account/{token}',
            **kwargs
        )

        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.session.get(
            url=f"{self.host}/v1/account",
            **kwargs
        )

        return response
