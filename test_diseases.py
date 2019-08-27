# test_bucketlist.py
import unittest
import os
import json
from app import create_app, db


class BucketlistTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.disease = {
            'disease_name': 'Dengue',
            'disease_signs': 'Extreme Fatigue',
            'disease_symptoms': 'Loss of appetite',
            'confirmatory_tests': 'Blood Test'
        }

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_disease_addition(self):
        """Test API can add a disease (POST request)"""
        res = self.client().post('/disease/', data=self.disease)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Dengue', str(res.data))

    def test_api_can_get_all_diseases(self):
        """Test API can get a disease (GET request)."""
        res = self.client().post('/disease/', data=self.disease)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/disease/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Dengue', str(res.data))

    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()