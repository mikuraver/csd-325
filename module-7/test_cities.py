# Rebecca Essenburg
# Assignment 7.2
# 2/22/26

# This code tests the location function in the
# city_functions.py file.

import unittest
from city_functions import format_location

class LocationTestCase(unittest.TestCase):
    # Tests for 'city_functions.py'.
    def test_city_country(self):
        # Does a regular city, country input work?
        formatted_location = format_location('Phoenix', 'United States')
        self.assertEqual(formatted_location, 'Phoenix, United States - Population Unknown, English')

if __name__ == '__main__':
    unittest.main()