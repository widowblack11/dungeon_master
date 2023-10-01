

def test_delete_v1_account_login_all(prepare_user, dm_api_facade, dm_db):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password

    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dm_db.activete_user_by_login(login=login)
    dm_api_facade.login.login_user(
        login=login,
        password=password
    )
    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    headers = {'X-Dm-Auth-Token': token}
    dm_api_facade.account.set_headers(headers=headers)
    dm_api_facade.login.set_headers(headers=headers)

    dm_api_facade.login.logout_user_from_all_devices(x_dm_auth_token=headers['X-Dm-Auth-Token'])
