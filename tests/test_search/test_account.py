import pytest
import pytest_asyncio.plugin

from apis.dm_api_account.account_pb2 import RegisterAccountRequest


def test_account(grpc_account):
    response = grpc_account.grpc_account.account(
        RegisterAccountRequest(
            login='12testаftd129',
            email='12teаsf9ww@mail.ru',
            password='12te9tаsfdt123111'
        )
    )


@pytest.mark.asyncio
async def test_account_async(grpc_account_async):
    response = await grpc_account_async.register_account(
        register_account_request=RegisterAccountRequest(
            login='12tesft4аftd129',
            email='12teа4sff9ww@mail.ru',
            password='12t4ef9tаsfdt123111'
        )
    )
    print(response)

