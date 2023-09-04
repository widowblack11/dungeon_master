import time

from dm_account_api.models.registration_model import Registration
from services.dm_account_api import DmApiAccount
from generic.heplpes.mailhog import MailhogApi
import structlog
from dm_account_api.models.user_envelope import UserRole
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)
login = "te3s4t_3535vev_132999014"


def test_put_v1_account_token():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = Registration(
        login=login,
        email="190939344342d4egghkdk@mail.ru",
        password="tt3443e30e2st_55vv_1399491"
    )
    api.account_api.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_last_email()
    response = api.account_api.put_v1_account_token(token=token, status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player],
            "status": None
        }
    ))

