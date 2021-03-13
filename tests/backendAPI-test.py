import unittest
from backendAPI import app
from multiprocessing import Process
import time


class AppTests(unittest.TestCase):

    def start_app(self):
        server = Process(target=app.run)
        server.start()
        return server

    def shutdown_app(self, server):
        server.terminate()
        server.join()

    def test_start_stop(self):
        server = self.start_app()
        time.sleep(10)
        self.shutdown_app(server)


if __name__ == "__main__":
    unittest.main()


