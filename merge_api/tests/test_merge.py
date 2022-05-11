from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app, routes

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_truth(self):
        truth = 'What movie made you cry?'
        response = self.client.post(url_for('truth'), json = {'truth': truth})
        self.assertEqual(response.status_code, 200)

    def test_dare(self):
        dare= 'Kiss the person to your left'
        response = self.client.post(url_for('dare'), json = {'dare': dare})
        self.assertEqual(response.status_code, 200)
