from web.pages.request_page import RequestPage
from utils.common import Common
from utils.testdata import TestData


def test_request_response_single_user(browser, base_general):
    """Отправляем api запрос GET через WEB флорму """
    data = {
        '$.data.id': TestData.NUMBER_GET_SINGLE_USER,
        '$.data.last_name': TestData.LAST_NAME[TestData.NUMBER_GET_SINGLE_USER],
        '$.data.first_name': TestData.FIRST_NAME[TestData.NUMBER_GET_SINGLE_USER]
    }
    page = RequestPage(browser)
    # открываем web страницу
    page.open(Common.BASE_URL)
    # кликаем на кнопку отправки запроса
    page.click_button(page.SINGLE_USER)
    # фиксируем полученный ответ в виде текста
    response = page.respons(page.RESPONS)
    # делаем assert полученных данных и ожидаемых
    base_general.asserts.check_response_jsonpath(response=response, data=data)

def test_create_user(browser, base_general):
    """Отправляем api запрос POST через WEB флорму """
    data = {
        '$.name': TestData.USERNAME[TestData.NUMBER_CREATE_USER],
        '$.job': TestData.JOB[TestData.NUMBER_CREATE_USER]
    }
    page = RequestPage(browser)
    # открываем web страницу
    page.open(Common.BASE_URL)
    # кликаем на кнопку отправки запроса
    page.click_button(page.CREATE_USER)
    # фиксируем полученный ответ в виде текста
    response = page.respons(page.RESPONS)
    # делаем assert полученных данных и ожидаемых
    base_general.asserts.check_response_jsonpath(response=response, data=data)


def test_update_user(browser, base_general):
    """Отправляем api запрос PUT через WEB флорму """
    data = {
        '$.name': TestData.USERNAME[TestData.NUMBER_UPDATE_USER],
        '$.job': TestData.JOB[TestData.NUMBER_UPDATE_USER]
    }
    page = RequestPage(browser)
    # открываем web страницу
    page.open(Common.BASE_URL)
    # кликаем на кнопку отправки запроса
    page.click_button(page.UPDATE_USER)
    # фиксируем полученный ответ в виде текста
    response = page.respons(page.RESPONS)
    # делаем assert полученных данных и ожидаемых
    base_general.asserts.check_response_jsonpath(response=response, data=data)

