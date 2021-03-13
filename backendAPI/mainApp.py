from flask import Flask, request
import backend

app = Flask(__name__)

database_name = 'RecipeSite'
# collection_name = 'recipes'

@app.route('/')
def index():
    return 'Harry and Emma\'s Recipe Project'


@app.route('/<collection_name>/<recipe_id>', methods=["GET"])
def view_recipe(collection_name, recipe_id):
    """return the recipe information for <recipe_id>"""
    db = backend.Database(database_name, collection_name)
    query = {"id": recipe_id}
    return db.retrieve_recipe(query)


@app.route('/<collection_name>/create_new', methods=["POST"])
def new_recipe(collection_name, recipe):
    """adding recipe to collection in database"""
    db = backend.Database(database_name, collection_name)
    recipe_id = db.create_recipe(recipe)
    view_recipe(recipe_id)

@app.route('/<collection_name>/', methods=["GET"])
def view_all(collection_name):
    """viewing all recipes in a collection"""
    db = backend.Database(database_name, collection_name)
    return db.retrieve_all()





