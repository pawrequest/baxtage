from loguru import logger
from neo4j import GraphDatabase, Query, Session


class Neo4jConnection:

    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None

        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def connected(self):
        return self.__driver.verify_connectivity()

    def close(self):
        if self.__driver is not None:
            logger.debug("Closing connection")
            self.__driver.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def query(self, query: str | Query, parameters: dict = None, db: Session = None):
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            return list(session.run(query, parameters))
        except Exception as e:
            print("Query failed:", e)
            raise e

