import time

from hamcrest import assert_that, has_properties

from dm_account_api.models import UserDetailsEnvelope
from generic.helpers.dm_db import DmDatabase
from services.dm_account_api import Facade

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "emadild_ddtx3fdde4-fdrdst00d888837"
    email = "в@9dmdaidddfxd3df-4lrdd.ru"
    password = "tteddddd2dfxd3dfrds-423fddвe2st8_25v0d2124v_139991"
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is False, f'User {login} was activated'
    response = api.account.activate_registered_user(login=login)

    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'

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


def test_post_v1_account_with_select():
    api = Facade(host='http://5.63.153.31:5051')
    login = "emadild_ddtx3fdde4-fdrdst00d888837"
    email = "в@9dmdaidddfxd3df-4lrdd.ru"
    password = "tteddddd2dfxd3dfrds-423fddвe2st8_25v0d2124v_139991"
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is False, f'User {login} was activated'

    db.activete_user_by_login(login=login)
    api.login.login_user(
        login=login,
        password=password
    )




