from requests import Response
from dm_account_api.models.registration_model import RegistrationModel
from dm_account_api.models.reset_password import ResetPasswordModel
from dm_account_api.models.change_email import ChangeEmailModel
from dm_account_api.models.change_password import ChangePasswordModel
from dm_account_api.models.user_details_envelope import UserDetailsEnvelope
from dm_account_api.models.user_envelope import UserEnvelope
from restclient.restclient import Restclient
from dm_account_api.models.user_envelope_model import UserEnvelopeModel


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )

        return response

    def post_v1_account_password(self, json: ResetPasswordModel, **kwargs) -> Response:
        """
        :param json reset_password
        Reset registered user password
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        :param json change_email
        Change registered user email
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePasswordModel, **kwargs) -> Response:
        """
        :param json change_password
        Change registered user password
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response

    def put_v1_account_token(self, token, **kwargs) -> Response:
        """
        Activate registered user
        :return:
        """

        response = self.client.put(
            path=f'/v1/account/{token}',
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path=f"/v1/account",
            **kwargs
        )
        UserDetailsEnvelope(**response.json())
        return response
