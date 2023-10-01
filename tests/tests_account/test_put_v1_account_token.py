from dm_account_api.model.registration import Registration
from dm_account_api.model.user_role import UserRole
from hamcrest import assert_that, has_properties


def test_put_v1_account_token(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    dm_api_facade.account_api.register(
        registration=Registration(
            login=login,
            email=email,
            password=password
    ))
    response = dm_api_facade.account.activate_registered_user(login=login)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole('Guest'), UserRole('Player')]
        }
    ))

