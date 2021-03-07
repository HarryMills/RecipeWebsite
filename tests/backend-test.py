import unittest
import backend


class TestBackendMethods(unittest.TestCase):

    def test_init(self):
        val = backend.Database
        self.assertIs(val, backend.Database)


if __name__ == '__main__':
    unittest.main()
