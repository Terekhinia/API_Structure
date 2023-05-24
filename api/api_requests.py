"""Модуль содержит базовый класс для отправки запросов"""

import requests
import logging

class Request:
    """Обертка для отправки запросов"""

    def __init__(self):
        self.url = ''
        self.headers = {}
        self.cookies = {}

    def custom_request(self, method, url, params=None, data=None, headers=None, cookies=None) -> requests.Response:
        """Кастомная функция по отправки запроса. todo добавить логирование и облагородить заголовки с куки
        
        Args:
            method: Метод запроса (GET, POST, ...)
            url: ссылка запроса
            params: 
            data: body запроса
            headers: заголовки
            cookies: куки
        
        Returns:
            response: объект результата запроса
        """
        response = requests.request(method=method, url=url, params=params, data=data, headers=self.headers, cookies=self.cookies)
        logging.info(print(f'--{response.request.url=}\n--{response.status_code=}\n--{response.text=}\n--{response=}'))
        return response
