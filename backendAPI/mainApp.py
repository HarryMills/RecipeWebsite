from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Harry and Emma\'s Recipe Project'


@app.route('/recipes/<recipe_id>', methods=["GET", "POST"])
def recipes(recipe_id):
    if request.method == "GET":
        """return the recipe information for <recipe_id>"""

    if request.method == "POST":
        """modify/update the information for <recipe_id>"""


def shutdown_server():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug server")
    func()


@app.route('/shutdown', methods=["GET"])
def shutdown():
    shutdown_server()
    return "Server is shutting down"

def start():
    app.run()
    return "starting up the app"

