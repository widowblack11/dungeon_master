import time

import structlog

from services.dm_account_api import DmApiAccount
from generic.heplpes.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "test_vvvv_139921",
        "email": "1299944dkdkdk@mail.ru",
        "password": "test_vvvv_139921"
    }
    response_create = api.account_api.post_v1_account(json=json)
    assert response_create.status_code == 201
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response_activate = api.account_api.put_v1_account_token(token=token)
    assert response_activate.status_code == 200
    json_login = {
        "login": "test_vvvv_139921",
        "password": "test_vvvv_139921",
        "rememberMe": False
    }
    response_login = api.login_api.post_v1_account_login(json_login)
    assert response_login.status_code == 200
