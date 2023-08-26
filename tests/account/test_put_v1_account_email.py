import time

from dm_account_api.helpers.variables import login, password
from services.dm_account_api import DmApiAccount
from services.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": login,
        "email": "8299944dkdkdk@mail.ru",
        "password": password
    }
    response_create = api.account.post_v1_account(json=json)
    assert response_create.status_code == 201
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response_activate = api.account.put_v1_account_token(token=token)
    assert response_activate.status_code == 200
    json_email = {
        "login": login,
        "password": password,
        "email": "other_email3@mail.ru"
    }
    response_change_email = api.account.put_v1_account_email(json=json_email)
    assert response_change_email.status_code == 200

