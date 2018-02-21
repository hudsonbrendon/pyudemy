import unittest
import requests_mock

from pyudemy import Udemy
from decouple import config


class UdemyTestCase(unittest.TestCase):

    def setUp(self):
        self.client_id = config('CLIENT_ID')
        self.client_secret = config('CLIENT_SECRET')
        self.udemy = Udemy(self.client_id, self.client_secret)

    def test_get_url(self):
        self.assertEqual(self.udemy._get_url('test'), 'https://www.udemy.com/api-2.0/test')

    def test_authentication(self):
        self.assertEqual(self.udemy._authentication.username, self.client_id)
        self.assertEqual(self.udemy._authentication.password, self.client_secret)

    @requests_mock.Mocker()
    def test_courses(self, request_mock):
        url = 'https://www.udemy.com/api-2.0/courses/'
        data = {
            'course': 'Test Course',
        }
        request_mock.get(url, json=data)
        self.assertEqual(self.udemy.courses(), data)


if __name__ == '__main__':
    unittest.main()
