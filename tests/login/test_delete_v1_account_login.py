import time

from services.dm_account_api import Facade


def test_delete_v1_account_login():
    api = Facade(host='http://5.63.153.31:5051')
    login = "em0ail_t3dex44fxxddst00d888837"
    email = "в@9ma-id3dxf44xlxdd.ru"
    password = "tt0ed2d3xd4xfxds423fddвe2st8_25v0d2124v_139991"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    time.sleep(2)
    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password
    )
    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)
    api.login.set_headers(headers=token)
    api.login.logout_user()
