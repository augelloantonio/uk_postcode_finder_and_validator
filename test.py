import unittest
from postcode.postcode import *

class TestPostcodeLibrary(unittest.TestCase):

    def test_postcode_is_valid(self):
        '''Test that the postcode is valid'''
        self.assertEqual(postcode_is_valid('CM77 8DR'), True)

    def test_get_postcode_status(self):
        ''' Test that the status is 200 (postcode found)'''
        self.assertEqual(get_data_postcode('CM77 8DR')['status'], 200)

    def test_nearby_postcode(self):
        '''Test get nearest postcodes''' 
        self.assertTrue(get_nearest_postcode("CW9 6GN"))


if __name__ == '__main__':
    unittest.main()