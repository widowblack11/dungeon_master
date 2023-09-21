

import structlog

from services.dm_account_api import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "tesf;d0w't[,p_vpvvv_139921"
    email = "12990fdw'9l,[4pp4dkdkdk@mail.ru"
    password = "te0dwf]/s,pp3kt_vvvv_139921"
    json = {
        "login": login,
        "email": email,
        "password": password
    }
    api.account_api.post_v1_account(json=json)
    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password
    )
