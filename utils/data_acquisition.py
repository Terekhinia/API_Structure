from web.pages.request_page import RequestPage
from utils.common import Common


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


