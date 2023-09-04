from dm_account_api.models import Registration


class Account:
    def __init__(self, facade):
        from services.dm_account_api import Facade
        self.facade: Facade = facade

    def register_new_user(self, login: str, email: str, password: str):
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def activate_registered_user(self):
        token = self.facade.mailhog.get_token_from_last_email()
        response = self.facade.account_api.put_v1_account_token(
            token=token
        )
        return response
