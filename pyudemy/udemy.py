import operator
from urllib.parse import quote

import requests
from requests.auth import HTTPBasicAuth


class Udemy(object):
    def __init__(self, client_id: str, client_secret: str):
        """Initialize Udemy class.
        Access token is required to make requests to the API.
        https://www.udemy.com/instructor/account/api/

        Args:
            client_id (str): Your client id.
            client_secret (str): Your client secret.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self._URL = "https://www.udemy.com/api-2.0/"

    def _get_url(self, resource: str, **kwargs) -> str:
        """Returns url for specified resource.

        Args:
            resource (str): Resource name.

        Returns:
            str: Url for specified resource.
        """
        url = f"{self._URL}{resource}/?"
        field_string = ""
        for param, value in sorted(kwargs.items(), key=operator.itemgetter(0)):
            if param != "fields":
                if (
                    "category" in param and "&" in value
                ):  # Patches unsupported categories that use &
                    value = value.replace(" & ", "+%26+")
                url += f"{param}={value}&"
            else:
                for ele in value:
                    object_name = ele["Object"]
                    params = ",".join(
                        filter(
                            None,
                            [
                                ele["Setting"],
                                ",".join(ele["Additions"]),
                                ",".join(["-" + x for x in ele["Minus"]]),
                            ],
                        )
                    )  # Can now use a fields parameter to control return info
                    field_string += f"fields[{object_name}]={params}&"
        url += field_string
        return url

    @property
    def _authentication(self) -> HTTPBasicAuth:
        """Returns authentication object.

        Returns:
            HTTPBasicAuth: Authentication object.
        """
        auth = HTTPBasicAuth(self.client_id, self.client_secret)
        return auth

    def courses(self, **kwargs) -> dict:
        """Returns list of courses.
        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/methods/get-courses-list/

        Returns:
            dict: List of courses.
        """
        courses = requests.get(
            self._get_url("courses", **kwargs), auth=self._authentication
        ).json()
        return courses

    def course_detail(self, id: int) -> dict:
        """Returns course with specified pk.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/methods/get-courses-detail/

        Args:
            id (int): Course id.

        Returns:
            dict: Course with specified pk.
        """
        course = requests.get(
            self._get_url(f"courses/{id}"), auth=self._authentication
        ).json()
        return course

    def public_curriculum(self, id: int, **kwargs) -> dict:
        """Returns list of curriculum items.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/methods/get-publiccurriculum-list/

        Args:
            id (int): Curriculum id.

        Returns:
            dict: List of curriculum items.
        """
        public_curriculum = requests.get(
            self._get_url(f"courses/{id}/public-curriculum-items"),
            auth=self._authentication,
        ).json()
        return public_curriculum

    def course_reviews(self, id: int, **kwargs) -> dict:
        """Returns list of reviews items.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/methods/get-publiccurriculum-list/

        Args:
            id (int): Course id.

        Returns:
            dict: List of reviews items.
        """
        reviews = requests.get(
            self._get_url(f"courses/{id}/reviews", **kwargs),
            auth=self._authentication,
        ).json()
        return reviews
