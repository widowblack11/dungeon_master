from hamcrest import assert_that, has_properties

from apis.dm_account_api.models.change_email import ChangeEmail


def test_put_v1_account(dm_api_facade, prepare_user):
    login = prepare_user.login
    email = prepare_user.email
    password = prepare_user.password
    json = ChangeEmail(
        login=login,
        email=email,
        password=password
    )
    dm_api_facade.account_api.post_v1_account(json=json)
    dm_api_facade.account.activate_registered_user(login=login)
    response = dm_api_facade.account.change_email_for_user(
        login=login,
        email="rtr2924f4gdddgdghkddk@mail.ru",
        password=password
    )
    assert_that(response.resource, has_properties(
        {
            "medium_picture_url": None,
            "location": None,
            "registration": None
        }
    ))

