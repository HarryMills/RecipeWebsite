import unittest
from backendAPI import app
from multiprocessing import Process
import time


# class AppTests(unittest.TestCase):
#     def start_app(self):
#         server = Process(target=app.run)
#         server.start()
#         return server
#
#     def shutdown_app(self, server):
#         server.terminate()
#         server.join()
#
# #     def test_start(self):
# #         server = self.start_app()
# #
# #     def test_shutdown(self):
# #         start()
# #         result = shutdown()
# #         self.assertEqual(result, "Server is shutting down")
# #
# #
# # if __name__ == "__main__":
# #     unittest.main()
#
def start():
    server = Process(target=app.run)
    server.start()
    return server


def shutdown(server):
    server.terminate()
    server.join()

server = start()
time.sleep(10)
shutdown(server)

