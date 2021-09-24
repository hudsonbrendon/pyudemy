import operator
from urllib.parse import quote

import requests
from requests.auth import HTTPBasicAuth


class Udemy(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self._URL = "https://www.udemy.com/api-2.0/{}/?"

    def _get_url(self, resource, **kwargs):
        url = self._URL.format(resource)
        for param, value in sorted(kwargs.items(), key=operator.itemgetter(0)):
            if value:

                # This 2 lines of code helps us to deal with spaces present in the arguements.
                if type(value) == str:
                    value = quote(value)

                url += "{}={}&".format(param, value)
        return url

    @property
    def _authentication(self):
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        return auth

    def courses(self, **kwargs):
        """
        Returns list of courses.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/methods/get-courses-list/
        """
        courses = requests.get(
            self._get_url("courses", **kwargs), auth=self._authentication
        ).json()
        return courses

    def course_detail(self, id):
        """
        Returns course with specified pk.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/methods/get-courses-detail/
        """
        course = requests.get(
            self._get_url("courses/{}".format(id)), auth=self._authentication
        ).json()
        return course

    def public_curriculum(self, id, **kwargs):
        """
        Returns list of curriculum items.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/methods/get-publiccurriculum-list/
        """
        public_curriculum = requests.get(
            self._get_url("courses/{}/public-curriculum-items".format(id)),
            auth=self._authentication,
        ).json()
        return public_curriculum

    def course_reviews(self, id, **kwargs):
        """
        Returns list of curriculum items.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/methods/get-publiccurriculum-list/
        """
        reviews = requests.get(
            self._get_url("courses/{}/reviews".format(id), **kwargs),
            auth=self._authentication,
        ).json()
        return reviews
