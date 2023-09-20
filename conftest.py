from collections import namedtuple

import pytest
import structlog
from vyper import v
from pathlib import Path

from generic.assertions.post_v1_account import AssertionsPostV1Account
from generic.helpers.mailhog import MailhogApi
from generic.helpers.orm_db import OrmDatabase
from services.dm_account_api import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture()
def mailhog():
    return MailhogApi(host=v.get('service.mailhog'))


@pytest.fixture()
def dm_api_facade(mailhog):
    return Facade(
        host=v.get('service.dm_api_account'),
        mailhog=mailhog
    )


options = (
    'service.dm_api_account',
    'service. mailhog',
    'database.dm3_5.host'
)


@pytest.fixture()
def dm_db():
    db = OrmDatabase(
        user=v.get('database.dm3_5.user'),
        password=v.get('database.dm3_5.password'),
        host=v.get('database.dm3_5.host'),
        database=v.get('database.dm3_5.database')
    )
    return db


@pytest.fixture
def assertions(dm_db):
    return AssertionsPostV1Account(dm_db)


@pytest.fixture
def prepare_user(dm_api_facade, dm_db):
    user = namedtuple('User', 'login, email, password')
    User = user(login=v.get('user.login'), email=v.get('user.email'), password=v.get('user.password'))
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()
    return User


@pytest.fixture(autouse=True)
def set_config(request):
    config = Path(__file__).parent.joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(option, request.config.getoption(f'--{option}'))


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)
