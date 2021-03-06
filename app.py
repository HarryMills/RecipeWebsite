from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Harry and Emma\'s Recipe Website'


if __name__ == "__main__":
    app.run()
