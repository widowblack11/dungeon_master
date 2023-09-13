import uuid

import records
import structlog
from sqlalchemy import create_engine

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class OrmClient:
    def __init__(self, user, password, host, database, isolation_level='AUTOCOMMIT'):
        connection_string = f"postgresql://{user}:{password}@{host}/{database}"
        self.engine = create_engine(connection_string, isolation_level=isolation_level)
        self.db = self.engine.connect()
        self.log = structlog.get_logger(self.__class__.__name__).bind(sevice='db')

    def close_connection(self):
        self.db.close()

    def send_query(self, query):
        print(query)
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            query=str(query)
        )
        dataset = self.db.execute(statement=query)
        log.msg(
            event='response',
            query=[dict(row) for row in dataset]
        )
        return dataset

    #def send_bulk_query(self, query):
    #    print(query)
    #    log = self.log.bind(event_id=str(uuid.uuid4()))
    #    log.msg(
    #        event='request',
    #        query=query
    #    )
    #    self.db.bulk_query(query=query)




