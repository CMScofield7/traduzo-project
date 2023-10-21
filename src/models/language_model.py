from .abstract_model import AbstractModel
from database.db import db


# Req. 1
class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict):
        super().__init__(data)

    # Req. 2
    def to_dict(self):
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"],
        }

    # Req. 3
    @classmethod
    def list_dicts(cls):
        data = cls._collection.find()
        return [cls(d).to_dict() for d in data]
