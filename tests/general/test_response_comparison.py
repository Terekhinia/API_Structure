from utils.data_acquisition import *


def test_assert_response_api_and_web(base_api, browser):
    # получение get response api методом
    test_get_response_api = data_acquisition_get_api(base_api, id_user=2)
    # получение get response через web
    test_get_response_web = data_acquisition_get_web(browser)
    api_response_str = str(test_get_response_api).replace(' ', '')
    web_response_str = str(test_get_response_web).replace(' ', '')
    assert web_response_str == api_response_str
