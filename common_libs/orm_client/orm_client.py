import uuid
from functools import wraps

import allure
import records
import structlog
from sqlalchemy import create_engine

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


class OrmClient:
    def __init__(self, user, password, host, database, isolation_level='AUTOCOMMIT'):
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        print(connection_string)
        self.engine = create_engine(connection_string, isolation_level=isolation_level)
        self.db = self.engine.connect()
        self.log = structlog.get_logger(self.__class__.__name__).bind(sevice='db')

    def close_connection(self):
        self.db.close()

    @allure_attach
    def send_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=str(query)
        )
        dataset = self.db.execute(statement=query)
        result = [row for row in dataset]
        log.msg(
            event='response',
            query=[dict(row) for row in result]
        )
        return result

    @allure_attach
    def send_bulk_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=str(query)
        )
        self.db.execute(statement=query)




