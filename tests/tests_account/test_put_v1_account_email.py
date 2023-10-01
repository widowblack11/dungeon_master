from dm_account_api.model.user_role import UserRole
from hamcrest import assert_that, has_properties


def test_post_v1_account(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dm_api_facade.account.activate_registered_user(login=login)
    response = dm_api_facade.account.change_email_for_user(
        login=login,
        email="rtr2924f4gdddgdghkddk@mail.ru",
        password=password
    )

    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole('Guest'), UserRole('Player')]
        }
    ))
