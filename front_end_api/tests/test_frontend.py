from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock
import requests_mock

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_truth(self):
        with requests_mock.Mocker() as m:
            m.get('http://truth_api:5000/get_truth', text="What is the dumbest thing you've ever cried over")
            m.post('http://merge_api:5000/post/truth', text='6 points')

            response = self.client.get(url_for('truth'))
            self.assertEqual(response.status_code, 200)

    def test_dare(self):
        with requests_mock.Mocker() as m:
            m.get('http://dare_api:5000/get_dare', text="Let the person on your left go through your phone")
            m.post('http://merge_api:5000/post/dare', text='10 points')

            response = self.client.get(url_for('dare'))
            self.assertEqual(response.status_code, 200)