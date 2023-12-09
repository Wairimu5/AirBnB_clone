#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the base_model
    """
    def test_str(self):
        """
        checks the string output of an instance
        """
        base = BaseModel()
        self.assertEqual(base.__str__(),
                         f"[{type(base).__name__}] \
({base.id}) {base.__dict__}")

    def test_to_dict(self):
    """
    checks the to_dict() function of an instance
    """
    base = BaseModel()
    prev_time = base.updated_at
    base_dict = base.to_dict()

    # Check if '__class__' key exists and its value is correct
    self.assertIn('__class__', base_dict)
    self.assertEqual(base_dict['__class__'], type(base).__name__)

    # Check if 'updated_at' and 'created_at' are formatted as expected
    self.assertIn('updated_at', base_dict)
    self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())
    self.assertIn('created_at', base_dict)
    self.assertEqual(base_dict['created_at'], base.created_at.isoformat())

    # Check if 'id' key exists and its value is correct
    self.assertIn('id', base_dict)
    self.assertEqual(base_dict['id'], base.id)

    base.save()
    self.assertNotEqual(prev_time, base.updated_at)


    def test_attr_classes(self):
        """
        checks if the right classes were use to generate attributes
        """
        base = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertNotEqual(base.id, base2.id)

    def test_save(self):
        """
        tests the save method
        """
        base = BaseModel()
        prevtime = base.updated_at
        base.save()
        newtime = base.updated_at
        self.assertNotEqual(prevtime, newtime)
