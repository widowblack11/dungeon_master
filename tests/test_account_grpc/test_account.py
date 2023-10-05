import pprint

import pytest
from betterproto import Casing

from apis.dm_api_account.account_pb2 import RegisterAccountRequest


def test_account(grpc_account, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    response = grpc_account.grpc_account.account(
        RegisterAccountRequest(
            login=login,
            email=email,
            password=password
        )
    )


@pytest.mark.asyncio
async def test_account_async(grpc_account_async, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    response = await grpc_account_async.register_account(
        register_account_request=RegisterAccountRequest(
            login=login,
            email=email,
            password=password
        )
    )
    pprint.pprint(response.to_dict())
