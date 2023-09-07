import time

from dm_account_api.models.registration_model import Registration

from services.dm_account_api import Facade

import structlog
from dm_account_api.models.user_envelope import UserRole
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)
login = "te3s4ftf_3535vev_132999014"


def test_put_v1_account_token():
    api = Facade(host='http://5.63.153.31:5051')
    json = Registration(
        login=login,
        email="1909ff39344342d4egghkdk@mail.ru",
        password="ttf3f443e30e2st_55vv_1399491"
    )
    api.account_api.post_v1_account(json=json)
    time.sleep(2)
    response = api.account.activate_registered_user(login=login)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player],
            "status": None
        }
    ))

