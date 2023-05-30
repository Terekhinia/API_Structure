from utils.data_acquisition import *


def test_assert_response_api_and_web(base_api, browser):
    """Позитивный тест"""
    # получение get response api методом
    test_get_response_api = data_acquisition_get_api(base_api, id_user=2)
    # получение get response через web
    test_get_response_web = data_acquisition_get_web(browser)
    # проверка полученных ответов
    assert_data_acquisition(test_get_response_api, test_get_response_web)



