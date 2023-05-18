"""Модуль содержит общие функции для работы с api"""

import jsonpath
import json


class Functions:

    @staticmethod
    def jsonpath(response, value):
        response_text = json.loads(response.text)
        response_value = jsonpath.jsonpath(response_text, f'$.{value}')[0]
        return response_value

