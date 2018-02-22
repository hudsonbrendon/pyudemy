import operator
import requests

from requests.auth import HTTPBasicAuth


class Udemy(object):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self._URL = 'https://www.udemy.com/api-2.0/{}/?'

    def _get_url(self, resource, **kwargs):
        url = self._URL.format(resource)
        for param, value in sorted(kwargs.items(), key=operator.itemgetter(0)):
            if value:
                url += '{}={}&'.format(param, value)
        return url

    @property
    def _authentication(self):
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        return auth

    def courses(self, **kwargs):
        courses = requests.get(self._get_url('courses', **kwargs), auth=self._authentication).json()
        return courses

    def course_detail(self, id):
        course = requests.get(self._get_url('courses/{}'.format(id)), auth=self._authentication).json()
        return course

    def course_reviews(self, id, **kwargs):
        reviews = requests.get(self._get_url('courses/{}/reviews'.format(id), **kwargs),
                               auth=self._authentication).json()
        return reviews
