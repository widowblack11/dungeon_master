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
    login = "emai7ddd2dl00409996e_t03ddde44fdjdst00d888837"
    email = "в@9m7ddda02i00490ed7d30dddf44lkdd.ru"
    password = "tt7dde20d4009d0ed072ddd3d4fmds423fddвe2st8_25v0d2124v_139991"
    new_password = "ttd8d3e002090d040ded72ddd3d4fmds423fddвe2st8_25v0d2124v_139991"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    time.sleep(2)
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
    api.account_api.put_v1_account_password(
        json=ChangePassword(
            login=login,
            token=str(token_in_body),
            oldPassword=password,
            newPassword=new_password
        )
    )







