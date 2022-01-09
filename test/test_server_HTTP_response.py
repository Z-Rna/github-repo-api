from unittest import TestCase
import requests
import os

class TestServerHTTPResponse(TestCase):
    localhost = 'http://127.0.0.1:5000'

    def test_home_page(self):
        '''

        Checks if page exists

        '''

        response = requests.get(f'{self.localhost}/')
        self.assertTrue(response.ok)

    def test_existing_endpoint(self):
        '''

        Check endpoint with response 200 OK

        '''
        endpoint = 'stars/z-rna'
        response = requests.get(f'{self.localhost}/{endpoint}')
        self.assertEqual(response.status_code, 200)

    def test_nonexisting_endpoint(self):
        '''

        Check endpoint with response 400 Not Found

        '''
        endpoint = 'wrong'
        response = requests.get(f'{self.localhost}/{endpoint}')
        self.assertEqual(response.status_code, 404)

    def test_POST_token_request(self):
        '''

        Check response of posted token

        '''

        endpoint = 'token/token_code'
        response = requests.post(f'{self.localhost}/{endpoint}')
        body = {
            "info": "Posted token",
            "token": "token_code"
        }
        requests.delete(f'{self.localhost}/token')
        self.assertEqual(response.json(), body)

