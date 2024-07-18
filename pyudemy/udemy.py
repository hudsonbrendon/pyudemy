import operator

import requests
from requests.auth import HTTPBasicAuth


class Udemy:
    __BASE_URL = "https://www.udemy.com/api-2.0/"

    def __init__(self, client_id: str, client_secret: str) -> None:
        """Initialize Udemy class.
        Access token is required to make requests to the API.
        https://www.udemy.com/instructor/account/api/

        Args:
            client_id (str): Your client id.
            client_secret (str): Your client secret.
        """
        self.__client_id = client_id
        self.__client_secret = client_secret

    @property
    def url(self) -> str:
        """Returns the base URL

        Returns:
            str: Base URL
        """
        return self.__BASE_URL

    @property
    def client_id(self) -> str:
        """Returns the client id

        Returns:
            str: Client id
        """
        return self.__client_id

    @property
    def client_secret(self) -> str:
        """Returns the client secret

        Returns:
            str: Client secret
        """
        return self.__client_secret

    def _get_full_url(self, resource: str, **kwargs) -> str:
        """Returns full url for specified resource.

        Args:
            resource (str): Resource name.

        Returns:
            str: Full url for specified resource.
        """
        url = f"{self.url}{resource}/?"
        field_string = ""
        for param, value in sorted(kwargs.items(), key=operator.itemgetter(0)):
            if param != "fields":
                if "category" in param and "&" in value:  # Patches unsupported categories that use &
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
        return HTTPBasicAuth(self.client_id, self.client_secret)


class UdemyAffiliate(Udemy):
    def courses(self, **kwargs) -> dict:
        """Returns list of courses.
        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/affiliate/methods/get-courses-list/

        Returns:
            dict: List of courses.
        """
        return requests.get(self._get_full_url("courses", **kwargs), auth=self._authentication).json()

    def course_detail(self, id: int) -> dict:
        """Returns course with specified id.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/affiliate/methods/get-courses-detail/

        Args:
            id (int): Course id.

        Returns:
            dict: Course with specified id.
        """
        return requests.get(self._get_full_url(f"courses/{id}"), auth=self._authentication).json()

    def public_curriculum(self, id: int, **kwargs) -> dict:
        """Returns list of curriculum items.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/affiliate/methods/get-publiccurriculum-list/

        Args:
            id (int): Curriculum id.

        Returns:
            dict: List of curriculum items.
        """
        return requests.get(
            self._get_full_url(f"courses/{id}/public-curriculum-items", **kwargs),
            auth=self._authentication,
        ).json()

    def course_reviews(self, id: int, **kwargs) -> dict:
        """Returns list of reviews items.

        To see the list of accepted parameters go to:
        https://www.udemy.com/developers/affiliate/methods/get-coursereviews-list/

        Args:
            id (int): Course id.

        Returns:
            dict: List of reviews items.
        """
        return requests.get(
            self._get_full_url(f"courses/{id}/reviews", **kwargs),
            auth=self._authentication,
        ).json()
