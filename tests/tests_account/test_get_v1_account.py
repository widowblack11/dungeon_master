from hamcrest import assert_that, has_properties

from apis.dm_account_api.models.user_details_envelope import UserRole


def test_get_v1_account(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
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
    response = dm_api_facade.account.get_current_user_info()
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player]
        }
    ))

## response = get_v1_account()
## print(response)
