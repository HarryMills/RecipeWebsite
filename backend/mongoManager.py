from pymongo import MongoClient


class MongoManager:
    def __init__(self, username, password):
        mongo_client_string = 'mongodb+srv://' + username + ':' + password + '@cluster0.qswd8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
        self.client = MongoClient(mongo_client_string)
        self.datebase = self.client["RecipeSite"]
        self.collection = self.datebase["recipe"]

    def server_info(self):
        return self.client.server_info()

