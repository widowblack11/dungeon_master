import time

from dm_account_api.models.registration_model import RegistrationModel
from services.dm_account_api import DmApiAccount
from services.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = RegistrationModel(
        login="test_55vv_1399914",
        email="199944d4gghkdk@mail.ru",
        password="ttest_55vv_1399491"
    )
    response_create = api.account.post_v1_account(json=json)
    assert response_create.status_code == 201, f'Статус код ответа должен быть равен 201, но он равен {response_create.status_code}'
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response_activate = api.account.put_v1_account_token(token=token)
    assert response_activate.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response_activate.status_code}'

