import os
from abc import ABC, abstractmethod
from typing import Any, Dict

import pymongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
from fastapi import Response, status

load_dotenv()


class ObjectNotFoundError(Exception):
    pass


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
        secrets = f"{self.user}:{self.pw}@{self.target}/{self.project}"
        return pymongo.MongoClient(
            f"mongodb+srv://{secrets}?retryWrites=true&w=majority"
        )

    def test_connection(self):
        return self.establish_connection().test

    def insert_one(self, schema: str, table: str, data: Dict[str, Any]):
        return self._connect_to_db(schema)[table].insert_one(data)

    def retrieve_one(self, schema: str, table: str, id: str) -> Dict[str, Any]:
        retrieved_object = self._connect_to_db(schema)[table].find_one(
            {"_id": ObjectId(id)}
        )
        if retrieved_object is None:
            raise ObjectNotFoundError(f"Object with id {id} not found")
        retrieved_object["_id"] = str(retrieved_object.get("_id"))
        return retrieved_object

    def _connect_to_db(self, schema: str):
        return self.establish_connection()[schema]


def create_db_conn() -> DatabaseConnection:
    return MongoDBConnection()


def get_chatlog(db_conn, id: str, response: Response):
    try:
        return db_conn.retrieve_one("Messages", "SubmittedMessage", id)
    except ObjectNotFoundError as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": str(e)}
