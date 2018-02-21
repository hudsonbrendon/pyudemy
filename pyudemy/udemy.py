import requests

from requests.auth import HTTPBasicAuth


class Udemy(object):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self._URL = 'https://www.udemy.com/api-2.0/{}'

    def _get_url(self, url):
        return self._URL.format(url)

    @property
    def _authentication(self):
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        return auth

    def courses(self, page=None, page_size=None, search=None, category=None,
                subcategory=None, price=None, is_affiliate_agreed=None,
                is_fixed_priced_deals_agreed=None, is_percentage_deals_agreed=None,
                language=None, has_closed_caption=None, has_coding_exercises=None,
                has_simple_quiz=None, instructional_level=None, ordering=None):
        courses = requests.get(self._get_url('courses/'), auth=self._authentication).json()
        return courses
