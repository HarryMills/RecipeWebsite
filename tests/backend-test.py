import unittest
import backend
import io
import sys

# Defined global variables for mongo database names used for unit tests
database_name = 'RecipeSite'
collection_name = 'recipe_test'


class TestBackendMethods(unittest.TestCase):

    def test_init(self):
        db = backend.Database(database_name, collection_name)
        self.assertIs(type(db), backend.Database)

    def test_create(self):
        db = backend.Database(database_name, collection_name)
        recipe = {"id": 1,
                  "name": "Burger o' Testing",
                  "ingredients": ["meat", "testing", "bun"]}
        val = db.create_recipe(recipe)
        self.assertIsNotNone(val)

    def test_retrieve(self):
        db = backend.Database(database_name, collection_name)
        query = {"id": 1}
        results = db.retrieve_recipe(query)
        for x in results:
            print(x)


    #def test_edit(self):

    #def test_delete(self):


if __name__ == '__main__':
    unittest.main()
