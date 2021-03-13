from flask import Flask, request
import backend

app = Flask(__name__)

database_name = 'RecipeSite'
collection_name = 'recipes'

@app.route('/')
def index():
    return 'Harry and Emma\'s Recipe Project'


@app.route('/recipes/<recipe_id>', methods=["GET"])
def view_recipe(recipe_id):
    """return the recipe information for <recipe_id>"""
    db = backend.Database(database_name, collection_name)
    query = {"id": recipe_id}
    return db.retrieve_recipe(query)


@app.route('/recipes/create_new', methods=["POST"])
def new_recipe(recipe):
    """adding recipe to the database. redirects to that recipe"""
    db = backend.Database(database_name, collection_name)
    recipe_id = db.create_recipe(recipe)
    view_recipe(recipe_id)


@app.route('/recipes/', methods=["GET"])
def view_all():
    """viewing all recipes on the site"""
    db = backend.Database(database_name, collection_name)
    return db.retrieve_all()


@app.route('/recipes/<recipe_id>', methods=["POST"])
def remove_recipe(recipe_id):
    """deleting a specific recipe. redirects to page with all recipes"""
    db = backend.Database(database_name, collection_name)
    query = {"id": recipe_id}
    val = db.delete_recipe(query)
    # do we need to do anything with val?? --> maybe for testing?
    view_all()


@app.route('/recipes/<recipe_id>', methods=["POST"])
def edit_recipe(recipe_id, data):
    """updating details for a specific recipe id, then gets edited recipe"""
    db = backend.Database(database_name, collection_name)
    query = {"id": recipe_id}
    result = db.edit_recipe(query, data)
    # do we need to do anything with result?? --> maybe for testing?
    view_recipe(recipe_id)




