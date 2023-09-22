import allure

from common_libs.db_client.db_client import DbClient


class DmDatabase:
    def __init__(self, user, password, host, database):
        self.db = DbClient(user, password, host, database)

    def get_all_users(self):
        with allure.step("Получить всех пользователей в БД"):
            query = 'select * from "public"."Users"'
            dataset = self.db.send_query(query=query)
            return dataset

    def get_user_by_login(self, login):
        with allure.step("Получить пользователя по логину"):
            query = f'''
            select * from "public"."Users"
            where "Login" = '{login}'
            '''
            dataset = self.db.send_query(query=query)
            return dataset

    def delete_user_by_login(self, login):
        with allure.step("Удалить в БД пользователя по логину"):
            query = f'''
            delete from "public"."Users"
            where "Login" = '{login}'
            '''
            dataset = self.db.send_bulk_query(query=query)
            return dataset

    def activete_user_by_login(self, login):
        with allure.step("Активировать в БД пользователя по логину"):
            query = f'''
            update "public"."Users"
            set "Activated" = True
            where "Login" = '{login}'
            '''
            dataset = self.db.send_bulk_query(query=query)
            return dataset
