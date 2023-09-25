from dm_account_api.models import LoginCredentials


class Login:
    def __init__(self, facade):
        from services.dm_account_api import Facade
        self.facade: Facade = facade

    def set_headers(self, headers):
        self.facade.login_api.client.session.headers.update(headers)

    def login_user(self, login: str, password: str, remember_me: bool = True):
        response = self.facade.login_api.post_v1_account_login(
            json=LoginCredentials(
                login=login,
                password=password,
                rememberMe=remember_me
            )
        )
        return response

    def get_auth_token(self, login: str, password: str, remember_me: bool = True):
        response = self.login_user(login=login, password=password, remember_me=remember_me)
        token = {'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}
        return token

    def logout_user(self, **kwargs):
        response = self.facade.login_api.delete_v1_account_login(**kwargs)
        return response

    def logout_user_from_all_devices(self, **kwargs):
        response = self.facade.login_api.delete_v1_account_delete(**kwargs)
        return response
