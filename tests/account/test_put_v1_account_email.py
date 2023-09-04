import time

from hamcrest import assert_that, has_properties

from dm_account_api.models.change_email import ChangeEmail
from services.dm_account_api import DmApiAccount
from generic.heplpes.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "test_5d5ddvv_2r13999131"
password = "ttedsddt_5r5vv_139991231"


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = ChangeEmail(
        login=login,
        email="113992d94rdd4dgghkdk@mail.ru",
        password=password
    )
    api.account_api.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    api.account_api.put_v1_account_token(token=token, status_code=200)
    json_email = ChangeEmail(
        login=login,
        email="rtr29244ddgdghkddk@mail.ru",
        password=password
    )
    response = api.account_api.put_v1_account_email(json=json_email)
    print(response)
    assert_that(response.resource, has_properties(
        {
            "medium_picture_url": None,
            "location": None,
            "registration": None
        }
    ))

