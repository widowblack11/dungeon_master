import pprint

import pytest
from betterproto import Casing

from apis.dm_api_account.account_pb2 import RegisterAccountRequest


def test_account(grpc_account):
    login = '12tef4fffffsdvt4fа6ftd129'
    response = grpc_account.grpc_account.account(
        RegisterAccountRequest(
            login=login,
            email='12t4fedff6аvfffsfrf9ww@mail.ru',
            password='12tevd4f6ffffff59tаsfdt123111'
        )
    )


@pytest.mark.asyncio
async def test_account_async(grpc_account_async):
    response = await grpc_account_async.register_account(
        register_account_request=RegisterAccountRequest(
            login='12t4eаffsrft4аftd129',
            email='124tfreаfа4sff9ww@mail.ru',
            password='142frаft4ef9tаsfdt123111'
        )
    )
    pprint.pprint(response.to_dict())
