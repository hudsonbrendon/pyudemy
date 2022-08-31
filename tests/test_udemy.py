from conftest import courses_with_params
from pyudemy import Udemy, __version__


def test_version():
    assert __version__ == "1.0.6"


class TestUdemy:
    def test_instance(self, udemy):
        assert isinstance(udemy, Udemy)

    def test_url(self, udemy):
        assert udemy.url == "https://www.udemy.com/api-2.0/"

    def test_client_id(self, udemy):
        assert udemy.client_id == "test"

    def test_client_secret(self, udemy):
        assert udemy.client_secret == "test"

    def test_get_full_url(self, udemy):
        assert udemy._get_full_url("courses") == "https://www.udemy.com/api-2.0/courses/?"
        assert (
            udemy._get_full_url("courses", page=1, page_size=1, search="javascript")
            == "https://www.udemy.com/api-2.0/courses/?page=1&page_size=1&search=javascript&"
        )

    def test_authentication(self, udemy):
        assert udemy._authentication.username == udemy.client_id
        assert udemy._authentication.password == udemy.client_secret

    def test_courses(self, requests_mock, udemy, courses):
        url = "https://www.udemy.com/api-2.0/courses/"
        requests_mock.get(url, json=courses)
        assert udemy.courses() == courses

    def test_courses_with_params(self, requests_mock, udemy, courses_with_params):
        url = "https://www.udemy.com/api-2.0/courses/?page=1&page_size=1"
        params = {
            "page": 1,
            "page_size": 1,
        }
        requests_mock.get(url, json=courses_with_params)
        assert udemy.courses(**params) == courses_with_params

    def test_courses_detail(self, requests_mock, udemy, course_detail):
        url = "https://www.udemy.com/api-2.0/courses/12345/"
        requests_mock.get(url, json=course_detail)
        assert udemy.course_detail(12345) == course_detail

    def test_public_curriculum(self, requests_mock, udemy, public_curriculum):
        url = "https://www.udemy.com/api-2.0/courses/12345/public-curriculum-items/"
        requests_mock.get(url, json=public_curriculum)
        assert udemy.public_curriculum(12345) == public_curriculum

    def test_public_curriculum_with_kwargs(self, requests_mock, udemy, public_curriculum_with_params):
        url = "https://www.udemy.com/api-2.0/courses/12345/public-curriculum-items/"
        params = {"page": 1, "page_size": 1}
        requests_mock.get(url, json=public_curriculum_with_params)
        assert udemy.public_curriculum(12345, **params) == public_curriculum_with_params

    def test_course_reviews(self, requests_mock, udemy, course_reviews):
        url = "https://www.udemy.com/api-2.0/courses/12345/reviews/"
        requests_mock.get(url, json=course_reviews)
        assert udemy.course_reviews(12345) == course_reviews

    def test_course_reviews_with_kwargs(self, requests_mock, udemy, courses_reviews_with_params):
        url = "https://www.udemy.com/api-2.0/courses/12345/reviews/?page=1&page_size=1"
        params = {"page": 1, "page_size": 1}
        requests_mock.get(url, json=courses_reviews_with_params)
        assert udemy.course_reviews(12345, **params) == courses_reviews_with_params
