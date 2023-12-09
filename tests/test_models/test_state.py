import unittest
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    def test_to_dict(self):
        # Test the to_dict() method
        state = State()
        state_dict = state.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at', 'name']
        self.assertCountEqual(state_dict.keys(), expected_keys)

        # Check if created_at and updated_at are in the expected format
        self.assertEqual(state_dict['created_at'], state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], state.updated_at.isoformat())

    def test_from_dict(self):
        # Test the instantiation from a dictionary representation
        state = State()
        state_dict = state.to_dict()
        new_state = State(**state_dict)
        self.assertEqual(new_state.id, state.id)
        self.assertEqual(new_state.created_at, state.created_at)
        self.assertEqual(new_state.updated_at, state.updated_at)
        self.assertEqual(new_state.name, state.name)
        # Add similar checks for other attributes

    def test_save(self):
        # Test the save method
        state = State()
        prev_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(prev_updated_at, state.updated_at)


if __name__ == "__main__":
    unittest.main()
