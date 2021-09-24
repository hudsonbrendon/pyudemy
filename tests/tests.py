import unittest

import requests_mock
from pyudemy import Udemy

from results import (COURSE_DETAIL, COURSE_REVIEWS, COURSES,
                     COURSES_REVIEWS_WITH_PARAMS, COURSES_WITH_PARAMS,
                     PUBLIC_CURRICULUM, PUBLIC_CURRICULUM_WITH_PARAMS)


class UdemyTestCase(unittest.TestCase):
    def setUp(self):
        self.client_id = "client_id"
        self.client_secret = "client_secret"
        self.udemy = Udemy(self.client_id, self.client_secret)

    def test_get_url(self):
        self.assertEqual(
            self.udemy._get_url("courses"), "https://www.udemy.com/api-2.0/courses/?"
        )
        self.assertEqual(
            self.udemy._get_url("courses", page=1, page_size=1, search="javascript"),
            "https://www.udemy.com/api-2.0/courses/?page=1&page_size=1&search=javascript&",
        )

    def test_authentication(self):
        self.assertEqual(self.udemy._authentication.username, self.client_id)
        self.assertEqual(self.udemy._authentication.password, self.client_secret)

    @requests_mock.Mocker()
    def test_courses(self, request_mock):
        url = "https://www.udemy.com/api-2.0/courses/"
        request_mock.get(url, json=COURSES)
        self.assertEqual(self.udemy.courses(), COURSES)

    @requests_mock.Mocker()
    def test_courses_with_kwargs(self, request_mock):
        url = "https://www.udemy.com/api-2.0/courses/?page=1&page_size=1"
        kwargs = {
            "page": 1,
            "page_size": 1,
        }
        request_mock.get(url, json=COURSES_WITH_PARAMS)
        self.assertEqual(self.udemy.courses(**kwargs), COURSES_WITH_PARAMS)

    @requests_mock.Mocker()
    def test_courses_detail(self, requests_mock):
        url = "https://www.udemy.com/api-2.0/courses/12345/"
        requests_mock.get(url, json=COURSE_DETAIL)
        self.assertEqual(self.udemy.course_detail(12345), COURSE_DETAIL)

    @requests_mock.Mocker()
    def test_public_curriculum(self, requests_mock):
        url = "https://www.udemy.com/api-2.0/courses/12345/public-curriculum-items/"
        requests_mock.get(url, json=PUBLIC_CURRICULUM)
        self.assertEqual(self.udemy.public_curriculum(12345), PUBLIC_CURRICULUM)

    @requests_mock.Mocker()
    def test_public_curriculum_with_kwargs(self, requests_mock):
        url = "https://www.udemy.com/api-2.0/courses/12345/public-curriculum-items/"
        kwargs = {"page": 1, "page_size": 1}
        requests_mock.get(url, json=PUBLIC_CURRICULUM_WITH_PARAMS)
        self.assertEqual(
            self.udemy.public_curriculum(12345, **kwargs), PUBLIC_CURRICULUM_WITH_PARAMS
        )

    @requests_mock.Mocker()
    def test_course_reviews(self, request_mock):
        url = "https://www.udemy.com/api-2.0/courses/12345/reviews/"
        request_mock.get(url, json=COURSE_REVIEWS)
        self.assertEqual(self.udemy.course_reviews(12345), COURSE_REVIEWS)

    @requests_mock.Mocker()
    def test_course_reviews_with_kwargs(self, request_mock):
        url = "https://www.udemy.com/api-2.0/courses/12345/reviews/?page=1&page_size=1"
        kwargs = {"page": 1, "page_size": 1}
        request_mock.get(url, json=COURSES_REVIEWS_WITH_PARAMS)
        self.assertEqual(
            self.udemy.course_reviews(12345, **kwargs), COURSES_REVIEWS_WITH_PARAMS
        )


if __name__ == "__main__":
    unittest.main()
