import requests

from requests.auth import HTTPBasicAuth


class Udemy(object):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.URL = 'https://www.udemy.com/api-2.0/'

    @property
    def _authentication(self):
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        return auth
