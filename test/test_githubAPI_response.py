from unittest import TestCase
import requests


class testgithubAPIResponse(TestCase):
    localhost = 'http://127.0.0.1:5000'

    def test_nonexisting_user(self):
        endpoint = 'stars/wrong-z-rna'
        response = requests.get(f'{self.localhost}/{endpoint}')
        self.assertEqual(response.status_code, 404)

    def test_star_count(self):
        endpoint = 'stars/z-rna'
        response = requests.get(f'{self.localhost}/{endpoint}')
        body = {
            "all_stars": 2,
            "user": "z-rna"
        }
        self.assertEqual(response.json(), body)
