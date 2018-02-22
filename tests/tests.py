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
        self.assertEqual(self.udemy._get_url('courses'), 'https://www.udemy.com/api-2.0/courses/?')
        self.assertEqual(self.udemy._get_url('courses', page=1, page_size=1, search='javascript'),
                         'https://www.udemy.com/api-2.0/courses/?page=1&page_size=1&search=javascript&')

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

    @requests_mock.Mocker()
    def test_courses_with_kwargs(self, request_mock):
        url = 'https://www.udemy.com/api-2.0/courses/?page=1&page_size=1'
        kwargs = {
            'page': 1,
            'page_size': 1,
        }
        data = {
            'course': 'Test Course',
        }
        request_mock.get(url, json=data)
        self.assertEqual(self.udemy.courses(**kwargs), data)

    @requests_mock.Mocker()
    def test_courses_detail(self, requests_mock):
        url = 'https://www.udemy.com/api-2.0/courses/12345/'
        data = {
            'course': 'Test Course',
        }
        requests_mock.get(url, json=data)
        self.assertEqual(self.udemy.course_detail(12345), data)

    @requests_mock.Mocker()
    def test_course_reviews(self, request_mock):
        url = 'https://www.udemy.com/api-2.0/courses/12345/reviews/'
        data = {
            'review': 'Test Review',
        }
        request_mock.get(url, json=data)
        self.assertEqual(self.udemy.course_reviews(12345), data)

    @requests_mock.Mocker()
    def test_course_reviews_with_kwargs(self, request_mock):
        url = 'https://www.udemy.com/api-2.0/courses/12345/reviews/?page=1&page_size=1'
        kwargs = {
            'page': 1,
            'page_size': 1
        }
        data = {
            'review': 'Test Review',
        }
        request_mock.get(url, json=data)
        self.assertEqual(self.udemy.course_reviews(12345, **kwargs), data)


if __name__ == '__main__':
    unittest.main()
