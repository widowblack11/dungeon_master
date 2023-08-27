import time

from dm_account_api.models.change_email import ChangeEmailModel
from dm_account_api.models.registration_model import RegistrationModel
from services.dm_account_api import DmApiAccount
from services.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "test_55vv_13999131"
password = "ttest_55vv_139991231"


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = RegistrationModel(
        login=login,
        email="113992944dgghkdk@mail.ru",
        password=password
    )
    response_create = api.account.post_v1_account(json=json)
    assert response_create.status_code == 201
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response_activate = api.account.put_v1_account_token(token=token)
    assert response_activate.status_code == 200
    json_email = ChangeEmailModel(
        login=login,
        email="13d9929244dgghkdk@mail.ru",
        password=password
    )
    response_change_email = api.account.put_v1_account_email(json=json_email)
    assert response_change_email.status_code == 200

