from sqlalchemy import select

from orm_client.orm_client import OrmClient
from generic.helpers.orm_models import User


class OrmDatabase:
    def __init__(self, user, password, host, database):
        self.db = OrmClient(user, password, host, database)

    def get_all_users(self):
        query = select([User])
        dataset = self.db.send_query(query)
        return dataset

    def get_user_by_login(self, login):
        query = select([User]).where(
            User.Login == login
        )
        dataset = self.db.send_query(query)
        return dataset
