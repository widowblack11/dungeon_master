import time

import structlog

from dm_account_api.models import ResetPassword, ChangePassword
from services.dm_account_api import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = Facade(host='http://5.63.153.31:5051')
    login = "test11fdf10d18010fs111hh"
    email = "10101ffd101d91@fgsmail.com"
    password = "101f1d10dsf9f10lslsl"
    new_password = "ls1fsdd9flsfl1ls1122"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password
    )
    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)
    api.account_api.post_v1_account_password(
        json=ResetPassword(
            login=login,
            email=email
        )
    )
    token_in_body = api.mailhog.get_reset_password_token_by_login(login=login)
    api.account.change_password(
        login=login,
        token=token_in_body,
        oldPassword=password,
        newPassword=new_password
    )








