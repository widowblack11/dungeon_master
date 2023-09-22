import uuid
from functools import wraps

import allure
import records
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def allure_attach(func):
    @wraps(func)
    def wrapper(self, query):
        allure.attach(
            str(query.compile(compile_kwargs={"literal_binds": True})),
            name='query',
            attachment_type=allure.attachment_type.TEXT
        )
        result = func(self, query)
        if result is not None:
            allure.attach(
                str(result),
                name='query_result',
                attachment_type=allure.attachment_type.TEXT
            )
        return result
    return wrapper


class DbClient:
    def __init__(self, user, password, host, database, isolation_level='AUTOCOMMIT'):
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        self.db = records.Database(connection_string, isolation_level=isolation_level)
        self.log = structlog.get_logger(self.__class__.__name__).bind(sevice='db')

    @allure_attach
    def send_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query
        )
        dataset = self.db.query(query=query).as_dict()
        log.msg(
            event='response',
            query=dataset
        )
        return dataset

    @allure_attach
    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=query
        )
        self.db.bulk_query(query=query)
