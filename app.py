from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Harry and Emma\'s Recipe Website'


@app.route('/recipes/<recipe_id>', methods=["GET", "POST"])
def recipes(recipe_id):
    if request.method == "GET":
        """return the recipe information for <recipe_id>"""

    if request.method == "POST":
        """modify/update the information for <recipe_id>"""

if __name__ == "__main__":
    app.run()
