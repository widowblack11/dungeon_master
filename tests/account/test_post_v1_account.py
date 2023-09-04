import time

from hamcrest import assert_that, has_properties

from dm_account_api.models import UserDetailsEnvelope
from services.dm_account_api import Facade

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "test2_53f5dsdvv_134d212909982"
    email = "12929f44ddgds3gh8k4ddk221@9mail.ru"
    password = "tte2s3fddst8_25v0d2124v_139991"
    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    time.sleep(2)
    response = api.account.activate_registered_user()
    assert_that(response.resource.rating, has_properties(
        {
            "enabled": True,
            "quality": 0,
            "quantity": 0
        }
    ))
    api.login.login_user(
        login=login,
        password=password
    )



