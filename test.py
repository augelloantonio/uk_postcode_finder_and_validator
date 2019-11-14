import unittest
from app import get_a_postcode, get_data_postcode

class TestLibrary(unittest.TestCase):

    def test_get_postcode(self):
        self.assertEqual(get_data_postcode('CM77 8DR')['status'], 200)

if __name__ == '__main__':
    unittest.main()