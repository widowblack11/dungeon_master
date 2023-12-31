from apis.dm_account_api.models import ResetPassword


def test_put_v1_account_password(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    new_password = "ls1fsdd9flsfl1ls1122"
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password,
        status_code=201
    )
    dm_api_facade.account.activate_registered_user(login=login)
    dm_api_facade.login.login_user(
        login=login,
        password=password
    )
    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.account_api.post_v1_account_password(
        json=ResetPassword(
            login=login,
            email=email
        )
    )
    token_in_body = dm_api_facade.mailhog.get_reset_password_token_by_login(login=login)
    old_password = password
    dm_api_facade.account.change_password(
        login=login,
        token=token_in_body,
        old_password=old_password,
        new_password=new_password
    )








