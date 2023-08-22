import time
from services.dm_account_api import DmApiAccount
from services.mailhog import MailhogApi


def test_put_v1_account_token():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "test_vvvv_1398",
        "email": "8944dkdkdk@mail.ru",
        "password": "test_vvvv_1398"
    }
    response_create = api.account.post_v1_account(json=json)
    assert response_create.status_code == 201
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response_activate = api.account.put_v1_account_token(token=token)
    assert response_activate.status_code == 200
