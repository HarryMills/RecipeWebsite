import unittest
from backendAPI import app, start, shutdown


class AppTests(unittest.TestCase):
    def test_start(self):
        result = start()
        self.assertEqual(result, "starting up the app")
        shutdown()

    def test_shutdown(self):
        start()
        result = shutdown()
        self.assertEqual(result, "Server is shutting down")


if __name__ == "__main__":
    unittest.main()

