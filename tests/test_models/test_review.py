import unittest
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    def test_to_dict(self):
        # Test the to_dict() method
        review = Review()
        review_dict = review.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at',
                         'place_id', 'user_id', 'text']
        self.assertCountEqual(review_dict.keys(), expected_keys)

        # Check if created_at and updated_at are in the expected format
        self.assertEqual(review_dict['created_at'],
                         review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'],
                         review.updated_at.isoformat())

    def test_from_dict(self):
        # Test the instantiation from a dictionary representation
        review = Review()
        review_dict = review.to_dict()
        new_review = Review(**review_dict)
        self.assertEqual(new_review.id, review.id)
        self.assertEqual(new_review.created_at, review.created_at)
        self.assertEqual(new_review.updated_at, review.updated_at)
        self.assertEqual(new_review.place_id, review.place_id)
        # Add similar checks for other attributes

    def test_save(self):
        # Test the save method
        review = Review()
        prev_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(prev_updated_at, review.updated_at)


if __name__ == "__main__":
    unittest.main()
