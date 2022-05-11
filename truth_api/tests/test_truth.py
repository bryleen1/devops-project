from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest

from application import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_truth(self):
       with patch('random.choice') as r:
           r.return_value = "What lie did you tell last?"
           response = self.client.get(url_for('truth'))
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'What lie did you tell last', response.data)