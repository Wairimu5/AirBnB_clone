#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_str(self):
        base1 = BaseModel()
        self.assertTrue(isinstance(base1, BaseModel))
