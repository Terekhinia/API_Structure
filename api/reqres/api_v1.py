"""Модуль содержит класс и методы с Api ручками"""

from .common import Common
from ..api_requests import Request

class ApiV1(Common):
    """Класс по работе с API"""

    def __init__(self):
        self.url = self.BASE_URL

    def get_api_users(self, id_user: int):
        """Пример ручки: https://reqres.in/api/users/2

        Args:
            id_user: id пользователя

        Returns:
            Тело ответа
        """

        url = f'{self.url}/api/users/{id_user}'
        # params = {'page': id_user}

        return Request().custom_request(method='GET', url=url)


    def post_api_created_users(self, data):
        """Пример ручки: https://reqres.in/api/users/

        Args:
            data: тело запроса

        Returns:
            Тело ответа
        """

        url = f'{self.url}/api/users/'

        return Request().custom_request(method='POST', url=url, data=data)


    def put_api_chains_users(self, data, id):
        """Пример ручки: https://reqres.in/api/users/

        Args:
            data: тело запроса

        Returns:
            Тело ответа
        """

        url = f'{self.url}/api/users/{id}'

        return Request().custom_request(method='PUT', url=url, data=data)
