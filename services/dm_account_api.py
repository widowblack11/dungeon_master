from dm_account_api.apis.account_api import AccountApi
from dm_account_api.apis.login_api import LoginApi
from generic.heplpes.login import Login
from generic.heplpes.mailhog import MailhogApi
from generic.heplpes.account import Account


class Facade:
    def __init__(self, host, mailhog_host=None, headers=None):
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = MailhogApi()
        self.account = Account(self)
        self.login = Login(self)

