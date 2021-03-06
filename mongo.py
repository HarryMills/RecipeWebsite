from pymongo import MongoClient

myclient = MongoClient('mongodb+srv://Harry:harry123@cluster0.qswd8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = myclient.RecipeSite

recipe = db.recipe

import datetime

recipeDocument = {
    "name": "Pizza",
    "date": str(datetime.date.today()),
    "ingredients": ["dough", "tomato", "mushroom", "pepperoni"],
    "category": "good"
}

recipe.insert_one(recipeDocument)

print(recipe.find_one({"name": "Pizza"}))


