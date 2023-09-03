import time

from hamcrest import assert_that, has_properties

from services.dm_account_api import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_account_api.models.registration_model import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = Registration(
        login="test2_5f5dvv_1399982",
        email="12929f44ddggh8kdk@mail.ru",
        password="tte2sfdt8_25vv_139991"
    )
    api.account.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token, status_code=200)
    assert_that(response.resource.rating, has_properties(
        {
            "enabled": True,
            "quality": 0,
            "quantity": 0
        }
    ))


