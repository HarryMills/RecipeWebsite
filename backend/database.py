from .mongoManager import MongoManager


class Database:
    def __init__(self):
        self.manager = MongoManager("Harry", "harry123")

    def createRecipe(self):
        print("create!")
        # TODO: Implement

    def retrieve_recipe(self):
        print("retrieve!")
        # TODO: Implement

    def edit_recipe(self):
        print("edit!")
        # TODO: Implement

    def delete_recipe(self):
        print("delete!")
        # TODO: Implement
