from collections import namedtuple

import pytest
import requests
import structlog

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
    return MailhogApi(host='http://5.63.153.31:5025')


@pytest.fixture()
def dm_api_facade(mailhog):
    return Facade(host='http://5.63.153.31:5051', mailhog=mailhog)


@pytest.fixture()
def dm_db():
    db = OrmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    return db


@pytest.fixture
def prepare_user(dm_api_facade, dm_db):
    user = namedtuple('User', 'login, email, password')
    User = user(login="tx3fdde4-fdrdst37", email='в@9dmtdxd.ru', password='ttetdddвe_139991')
    dm_db.delete_user_by_login(login=User.login)
    dataset = dm_db.get_user_by_login(login=User.login)
    assert len(dataset) == 0
    dm_api_facade.mailhog.delete_all_messages()
    return User



