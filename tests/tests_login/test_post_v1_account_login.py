
def test_post_v1_account(prepare_user, dm_api_facade, dm_db):
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
