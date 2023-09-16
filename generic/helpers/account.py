from dm_account_api.models import Registration, ChangeEmail, ChangePassword


class Account:
    def __init__(self, facade):
        from services.dm_account_api import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str, status_code):
        response = self.facade.account_api.post_v1_account(
            status_code=status_code,
            json=Registration(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(
            token=token
        )
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def change_email_for_user(self, login: str, email: str, password: str):
        response = self.facade.account_api.put_v1_account_email(
            json=ChangeEmail(
                login=login,
                email=email,
                password=password
            ))
        return response

    def get_token_from_email_for_change_password(self, login: str):
        token_for_request_body = str(self.facade.mailhog.get_reset_password_token_by_login(login=login))
        return token_for_request_body

    def change_password(self, token: str, login: str, old_password: str, new_password: str):
        response = self.facade.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=token,
                oldPassword=old_password,
                newPassword=new_password
            ))
        return response
