from services.dm_account_api import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
            "login": "test_vvvv_131",
            "email": "944dkdkdk@mail.ru",
            "password": "test_vvvv_131"
        }
    response_create = api.account.post_v1_account(
        json=json
    )
    assert response_create.status_code == 201
    response_activate = api.account.put_v1_account_token()
    assert response_activate.status_code == 200
