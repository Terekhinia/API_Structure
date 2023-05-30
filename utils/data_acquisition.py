"""
Модуль содержит функции по подготовке данных для проведения теста-сравнения ответов через вэб и апи
"""

from web.pages.request_page import RequestPage
from utils.common import Common
import logging

def data_acquisition_get_api(base_api, id_user):
        # Шаг 1. Запрос к апи
        api_response = base_api.api_v1.get_api_users(id_user=id_user).text
        return api_response

def data_acquisition_get_web(browser):
        page = RequestPage(browser)
        # открываем web страницу
        page.open(Common.BASE_URL)
        # кликаем на кнопку отправки запроса
        page.click_button(page.SINGLE_USER)
        # фиксируем полученный ответ в виде текста
        web_response = page.respons(page.RESPONS)
        return web_response

def assert_data_acquisition(response_get_api, response_get_web):
        api_response_str = str(response_get_api).replace(' ', '')
        web_response_str = str(response_get_web).replace(' ', '')
        msg = "Ответы не совпадают"
        logging.info(print(f'--{api_response_str=}\n--{web_response_str=}'))
        assert web_response_str == api_response_str, msg