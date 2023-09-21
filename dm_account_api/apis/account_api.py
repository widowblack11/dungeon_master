import allure
from requests import Response
from ..models import *
from restclient.restclient import Restclient
from ..utilities import validation_request_json, validate_status_code


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(
            self,
            json: Registration,
            status_code: int = 201,
            **kwargs
    ) -> Response:
        """
        :param status_code:
        :param json registration_model
        Register new user
        :return:
        """
        with allure.step("Регистрация нового пользователя"):
            response = self.client.post(
                path=f"/v1/account",
                json=validation_request_json(json),
                **kwargs
            )
            validate_status_code(response, status_code)
            return response

    def post_v1_account_password(
            self,
            json: ResetPassword,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json reset_password
        Reset registered user password
        :return:
        """
        with allure.step("Сбросить пароль зарегистрированного пользователя"):
            response = self.client.post(
                path=f"/v1/account/password",
                json=validation_request_json(json),
                **kwargs
            )
            validate_status_code(response, status_code)
            #if response.status_code == 201:
            #    return UserEnvelope(**response.json())
            return response

    def put_v1_account_email(
            self,
            json: ChangeEmail,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json change_email
        Change registered user email
        :return:
        """
        with allure.step("Изменить электронную почту у зарегистрированного пользователя"):
            response = self.client.put(
                path=f"/v1/account/email",
                json=validation_request_json(json),
                **kwargs
            )
            validate_status_code(response, status_code)
            if response.status_code == 200:
                return UserEnvelope(**response.json())
            return response

    def put_v1_account_password(
            self,
            json: ChangePassword,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param status_code:
        :param json change_password
        Change registered user password
        :return:
        """
        with allure.step("Сбросить пароль"):
            response = self.client.put(
                path=f"/v1/account/password",
                json=validation_request_json(json),
                **kwargs
            )
            validate_status_code(response, status_code)
            if response.status_code == 200:
                return UserEnvelope(**response.json())
            return response

    def put_v1_account_token(
            self,
            token,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserEnvelope:
        """
        :param token:
        :param status_code:
        Activate registered user
        :return:
        """
        with allure.step("Активировать пользователя"):
            response = self.client.put(
                path=f'/v1/account/{token}',
                **kwargs
            )
            validate_status_code(response, status_code)
            if response.status_code == 200:
                return UserEnvelope(**response.json())
            return response

    def get_v1_account(
            self,
            status_code: int = 200,
            **kwargs
    ) -> Response | UserDetailsEnvelope:
        """
        :param status_code:
        Get current user
        :return:
        """
        with allure.step("Получить данные по пользователю"):
            response = self.client.get(
                path=f"/v1/account",
                **kwargs
            )
            validate_status_code(response, status_code)
            if response.status_code == 200:
                return UserDetailsEnvelope(**response.json())
            return response
