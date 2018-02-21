import requests

from requests.auth import HTTPBasicAuth


class Udemy(object):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.URL = 'https://www.udemy.com/api-2.0/'

    def _pagination(self, pages):
        if pages > 100:
            raise ValueError('the maximum number of pages is 100')

    @property
    def _authentication(self):
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        return auth
