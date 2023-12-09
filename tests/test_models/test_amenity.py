#!/usr/bin/python3
"""
Test suite for amenity class
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_str(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        amenity = Amenity(name="Test Amenity")
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(amenity.id, amenity.name))

    def test_parent(self):
        amenity = Amenity()
        self.assertTrue(isinstance(amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
