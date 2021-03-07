import flask_unittest
from backendAPI import app


class AppTests(flask_unittest.AppTestCase):
    def start(self):
        app.run()

#
# if __name__ == "__main__":
#     # sys.path.append("..")
#     flask_unittest.main()

