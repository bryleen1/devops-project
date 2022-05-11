from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest

from application import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_dare(self):
       with patch('random.choice') as r:
           r.return_value = "Kiss the person next to you"
           response = self.client.get(url_for('dare'))
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'Kiss the person next to you', response.data)