from dm_account_api.services.dm_account_api import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    response = api.account.put_v1_account_token()
    assert response.status_code == 200