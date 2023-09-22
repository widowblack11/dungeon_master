from typing import List

import allure
from sqlalchemy import select, delete, update

from common_libs.orm_client.orm_client import OrmClient
from generic.helpers.orm_models import User


class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    def get_all_users(self) -> List[User]:
        with allure.step("Получить всех пользователей в БД"):
            query = select([User])
            dataset = self.db.send_query(query)
            return dataset

    def get_user_by_login(self, login) -> List[User]:
        with allure.step("Получить пользователя из БД по логину"):
            query = select([User]).where(
                User.Login == login
            )
            dataset = self.db.send_query(query)
            return dataset

    def delete_user_by_login(self, login):
        with allure.step("Удалить пользователя в БД по логину"):
            query = delete(User).where(
                User.Login == login
            )
            dataset = self.db.send_bulk_query(query=query)
            return dataset

    def activete_user_by_login(self, login):
        with allure.step("Активация пользователя"):
            query = update(User).where(User.Login == login).values(Activated=True)
            dataset = self.db.send_bulk_query(query=query)
            return dataset
