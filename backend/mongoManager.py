from pymongo import MongoClient


class MongoManager:
    def __init__(self, username, password, database, collection):
        mongo_client_string = 'mongodb+srv://' + username + ':' + password + '@cluster0.qswd8.mongodb.net' \
                                                                             '/myFirstDatabase?retryWrites=true&w' \
                                                                             '=majority'
        self.client = MongoClient(mongo_client_string)
        dblist = self.client.list_database_names()
        if database in dblist:
            self.database = self.client[database]
            collectionlist = self.database.list_collection_names()
            if collection in collectionlist:
                self.collection = self.database[collection]
            else:
                print("Collection doesn't exist in database")
        else:
            print("Database doesn't exist")

    def server_info(self):
        return self.client.server_info()

    def get_databases(self):
        return self.client.list_database_names()

    def get_collections(self, database):
        return self.client[database].list_collection_names()
