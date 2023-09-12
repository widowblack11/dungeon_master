import time

from hamcrest import assert_that, has_properties

from dm_account_api.models.change_email import ChangeEmail

import structlog

from services.dm_account_api import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

login = "test_5gd5ddvvf_2rc13999131"
password = "ttedgsddt_f5r5cvv_139991231"


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    json = ChangeEmail(
        login=login,
        email="113992gdf94rcdd4dgghkdk@mail.ru",
        password=password
    )
    api.account_api.post_v1_account(json=json)
    api.account.activate_registered_user(login=login)
    response = api.account.change_email_for_user(
        login=login,
        email="rtr2924f4gddgdghkddk@mail.ru",
        password=password
    )
    assert_that(response.resource, has_properties(
        {
            "medium_picture_url": None,
            "location": None,
            "registration": None
        }
    ))

