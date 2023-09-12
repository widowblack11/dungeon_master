import time

import structlog

from services.dm_account_api import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "emadidl_ft3xdse4f4fddst00d888837"
    email = "в@9dmdaifd3sxdf4f4ldd.ru"
    password = "ttddefd2sxd3df4fds423fddвe2st8_25v0d2124v_139991"
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
    api.account.get_current_user_info()




## response = get_v1_account()
## print(response)
