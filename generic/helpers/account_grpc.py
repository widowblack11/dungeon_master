from apis.dm_api_account.account_pb2 import RegisterAccountRequest
from apis.dm_api_account.dm_api_account import DmApiAccount


class AccountGrpc:
    def __init__(self, target):
        self.grpc_account = DmApiAccount(target=target)

    def account(self, login: str, email: str, password: str):
        response = self.grpc_account.account(
            request=RegisterAccountRequest(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def close(self):
        self.grpc_account.close()
