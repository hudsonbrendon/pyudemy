from pyudemy import Udemy, __version__


def test_version():
    assert __version__ == "1.1.2"


class TestUdemy:
    def test_instance(self, udemy) -> None:
        assert isinstance(udemy, Udemy)

    def test_url(self, udemy) -> None:
        assert udemy.url == "https://www.udemy.com/api-2.0/"

    def test_client_id(self, udemy) -> None:
        assert udemy.client_id == "test"

    def test_client_secret(self, udemy) -> None:
        assert udemy.client_secret == "test"

    def test_get_full_url(self, udemy) -> None:
        assert udemy._get_full_url("courses") == "https://www.udemy.com/api-2.0/courses/?"
        assert (
            udemy._get_full_url("courses", page=1, page_size=1, search="javascript")
            == "https://www.udemy.com/api-2.0/courses/?page=1&page_size=1&search=javascript&"
        )

    def test_authentication(self, udemy) -> None:
        assert udemy._authentication.username == udemy.client_id
        assert udemy._authentication.password == udemy.client_secret


class TestUdemyAffiliate:
    def test_instance(self, udemy_affiliate) -> None:
        assert isinstance(udemy_affiliate, Udemy)

    def test_courses(self, udemy_affiliate) -> None:
        assert isinstance(udemy_affiliate.courses(), dict)

    def test_course_detail(self, udemy_affiliate) -> None:
        assert isinstance(udemy_affiliate.course_detail(28295), dict)

    def test_public_curriculum(self, udemy_affiliate) -> None:
        assert isinstance(udemy_affiliate.public_curriculum(28295), dict)

    def test_course_reviews(self, udemy_affiliate) -> None:
        assert isinstance(udemy_affiliate.course_reviews(28295), dict)
