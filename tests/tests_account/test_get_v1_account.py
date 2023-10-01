def test_get_v1_account(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dm_api_facade.account.activate_registered_user(login=login)
    dm_api_facade.login.login_user(
        login=login,
        password=password
    )
    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    headers = {'X-Dm-Auth-Token': token}
    dm_api_facade.account.set_headers(headers=headers)
    dm_api_facade.account.get_current_user_info(x_dm_auth_token=headers['X-Dm-Auth-Token'])




## response = get_v1_account()
## print(response)
