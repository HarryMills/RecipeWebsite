from .mongoManager import MongoManager


class Database:
    def __init__(self):
        self.manager = MongoManager("Harry", "harry123")

    def create_recipe(self, data):
        val = self.manager.collection.insert_one(data)
        return val.inserted_id

    def retrieve_recipe(self, query):
        # Example query could be a dictionary like below:
        # myquery = {"id": "0001"}
        results = self.manager.collection.find(query)
        return results

    def edit_recipe(self, query, data):
        result = self.manager.collection.update_one(query, data)
        return result.acknowledged

    def delete_recipe(self, query):
        val = self.manager.collection.delete_one(query)
        return val.deleted_count
