import random
from string import ascii_letters, digits

import allure
import pytest
from hamcrest import assert_that, has_entries


def random_string(begin=1, end=30):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(random.randint(begin, end)):
        string += random.choice(symbols)
    return string


@allure.suite("Тесты на проверку метода POST{host}/v1/account")
@allure.sub_suite("Позитивные проверки")
class TestPostV1Account:
    @allure.title("Проверка создания и активации пользователя")
    def test_post_v1_account(self, dm_api_facade, dm_db, prepare_user, assertions):
        """
        Тест проверяет создание и активацию пользователя в базе данных
        """
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password
        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=201
        )
        dataset = dm_db.get_user_by_login(login=login)
        assertions.check_user_was_created(login=login)
        # for row in dataset:
        #     assert_that(row, has_entries(
        #         {
        #             'Login': login,
        #             'Activated': False
        #         }
        #     ))
            # assert row.Login == login, f'User {login} not registered'
            # assert row.Activated is False, f'User {login} was activated'

        # response = dm_api_facade.account.activate_registered_user(login=login)

        dm_db.activete_user_by_login(login=login)

        assertions.check_user_was_activated(login=login)
        # assert_that(response.resource.rating, has_properties(
        #    {
        #        "enabled": True,
        #        "quality": 0,
        #        "quantity": 0
        #    }
        # ))

        dm_api_facade.login.login_user(
            login=login,
            password=password
        )

    def test_post_v1_account_with_select(self, dm_api_facade, dm_db, prepare_user, assertions):
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password

        dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=201
        )
        assertions.check_user_was_created(login=login)

        dm_db.activete_user_by_login(login=login)
        assertions.check_user_was_activated(login=login)
        dm_api_facade.login.login_user(
            login=login,
            password=password
        )

    @pytest.mark.parametrize('login, email, password, status_code,check', [
        ('12', '12@12.ru', '123456', 201, ''),
        ('12', '12@12.ru', random_string(1, 5), 400, {"Password": ["Short"]}),
        ('1', '12@12.ru', '123456', 400, {"Login": ["Short"]}),
        ('12', '12@', '123456', 400, {"Email": ["Invalid"]}),
        ('12', '12', '123456', 400, {"Email": ["Invalid"]})
    ])
    def test_create_and_activated_user_with_random_params(
            self,
            dm_api_facade,
            dm_db,
            login,
            email,
            password,
            status_code,
            check,
            assertions
    ):
        dm_db.delete_user_by_login(login=login)
        dm_api_facade.mailhog.delete_all_messages()
        response = dm_api_facade.account.register_new_user(
            login=login,
            email=email,
            password=password,
            status_code=status_code
        )
        if status_code == 201:
            dm_api_facade.account.activate_registered_user(login=login)
            dataset = dm_db.get_user_by_login(login=login)
            assertions.check_user_was_activated(login=login)
            dm_api_facade.login.login_user(
                login=login,
                password=password
            )
        else:
            assert response.json()['errors'] == check, \
                f'Тело ответа должно быть равно {check}, но он равен {response}'
