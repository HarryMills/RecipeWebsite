from .mongoManager import MongoManager


class Database:
    def __init__(self):
        self.manager = MongoManager("Harry", "harry123")

    def create_recipe(self, data):
        val = self.manager.collection.insert_one(data)
        return val.inserted_id

    def retrieve_recipe(self, data):
        print("retrieve!")
        # TODO: Implement

    def edit_recipe(self, data):
        print("edit!")
        # TODO: Implement

    def delete_recipe(self, data):
        val = self.manager.collection.delete_one(data)
        return val.deleted_count
