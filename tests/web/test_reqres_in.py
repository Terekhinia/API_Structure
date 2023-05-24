from web.pages.request_page import RequestPage
from web.base.base_page import BasePage
from utils.common import Common
from utils.testdata import TestData
import time

def test_request_response_single_user_2(browser, base_general):
    """Отправляем api запрос GET через WEB флорму """
    id_user = 2
    data = {
        '$.data.id': id_user,
        '$.data.last_name': TestData.LAST_NAME[id_user],
        '$.data.first_name': TestData.FIRST_NAME[id_user]
    }
    page = RequestPage(browser)
    base_page = BasePage(browser)
    # открываем web страницу
    base_page.open(Common.BASE_URL)
    # кликаем на кнопку отправки запроса
    page.click_button_get_single_user()
    # фиксируем полученный ответ в виде текста
    response = page.get_respons_single_user()
    # делаем assert полученных данных и ожидаемых
    base_general.asserts.check_response_jesonpath(response=response, data=data)

def test_create_user(browser, base_general):
    """Отправляем api запрос POST через WEB флорму """
    number_user = 1
    data = {
        '$.name': TestData.USERNAME[number_user],
        '$.job': TestData.JOB[number_user]
    }
    page = RequestPage(browser)
    base_page = BasePage(browser)
    # открываем web страницу
    base_page.open(Common.BASE_URL)
    # кликаем на кнопку отправки запроса
    page.click_button_post_user()
    time.sleep(1)
    # фиксируем полученный ответ в виде текста
    response = page.post_user()
    # делаем assert полученных данных и ожидаемых
    base_general.asserts.check_response_jesonpath(response=response, data=data)


def test_update_user(browser, base_general):
    """Отправляем api запрос PUT через WEB флорму """
    number_user = 2
    data = {
        '$.name': TestData.USERNAME[number_user],
        '$.job': TestData.JOB[number_user]
    }
    page = RequestPage(browser)
    base_page = BasePage(browser)
    # открываем web страницу
    base_page.open(Common.BASE_URL)
    page.click_button_put_user()
    time.sleep(1)
    # фиксируем полученный ответ в виде текста
    response = page.put_user()
    # делаем assert полученных данных и ожидаемых
    base_general.asserts.check_response_jesonpath(response=response, data=data)

