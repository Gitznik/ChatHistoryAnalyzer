import os
from abc import ABC, abstractmethod
from typing import Any, Dict

import pymongo
from dotenv import load_dotenv

load_dotenv()


class DatabaseConnection(ABC):
    @abstractmethod
    def establish_connection(self):
        pass

    @abstractmethod
    def insert_one(self, schema: str, table: str, data: Dict[str, Any]):
        pass

    @abstractmethod
    def retrieve_one(self, schema: str, table: str, data: Dict[str, Any]):
        pass

    @abstractmethod
    def test_connection(self, schema: str, table: str, data: Dict[str, Any]):
        pass


class MongoDBConnection(DatabaseConnection):
    user: str = os.environ["MONGODB_USER"]
    pw: str = os.environ["MONGODB_PW"]
    target: str = os.environ["MONGODB_TARGET"]
    project: str = os.environ["MONGODB_PROJECT"]

    def establish_connection(self):
        return pymongo.MongoClient(
            f"mongodb+srv://{self.user}:{self.pw}@{self.target}/{self.project}?retryWrites=true&w=majority"
        )

    def test_connection(self):
        return self.establish_connection().test

    def insert_one(self, schema: str, table: str, data: Dict[str, Any]):
        return self._connect_to_db(schema)[table].insert_one(data)

    def retrieve_one(self, schema: str, table: str, data: Dict[str, Any]):
        return self._connect_to_db(schema)[table].find_one(data)

    def _connect_to_db(self, schema: str):
        return self.establish_connection()[schema]
