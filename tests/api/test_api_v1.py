import pytest
from utils.testdata import TestData

@pytest.mark.parametrize('id_user',
                         [2,
                          3])
def test_get_reqest_user(base_api, base_general, id_user):
    """Позитивный тест.

    Шаг 1. Отправка запроса. Пример: GET https://reqres.in/api/users/2
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    """

    # Шаг 1. Запрос к апи
    response = base_api.api_v1.get_api_users(id_user=id_user)

    # Шаг 2. Проверка статус кода
    base_api.asserts.check_status_code(status_code=response.status_code, exp_status_code=200)

    # Шаг 3. Проверка тела ответа
    data = {
        '$.data.id': id_user,
        '$.data.last_name': TestData.LAST_NAME[id_user],
        '$.data.first_name': TestData.FIRST_NAME[id_user]
    }
    base_general.asserts.check_response_jsonpath(response=response.text, data=data)


@pytest.mark.parametrize('id_user',
                         [1])
def test_post_create_user1(base_api, base_general, id_user):
    """Позитивный тест.

    Шаг 1. Отправка запроса. Пример: POST https://reqres.in/api/users
                                          Body {
                                               "name": "morpheus",
                                               "job": "leader"
                                                }
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    """

    # Шаг 1. Запрос к апи
    body = base_general.testdata.body_request(id_user)
    response = base_api.api_v1.post_api_created_users(data=body)

    # Шаг 2. Проверка статус кода
    base_general.asserts.check_status_code(status_code=response.status_code, exp_status_code=201)

    # Шаг 3. Проверка тела ответа
    data = {
        '$.username': TestData.USERNAME[id_user],
        '$.email': TestData.JOB[id_user]
    }
    base_general.asserts.check_response_jsonpath(response=response.text, data=data)


@pytest.mark.parametrize('id_user',
                         [2])
def test_put_change_user(base_api, base_general, id_user):
    """Позитивный тест.

    Шаг 1. Отправка запроса. Пример: PUT https://reqres.in/api/users
                                         Body {
                                              "name": "morpheus",
                                              "job": "zion resident"
                                         }
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    """

    # Шаг 1. Запрос к апи
    body = base_general.testdata.body_request(id_user)
    response = base_api.api_v1.put_api_chains_users(data=body, id=id_user)

    # Шаг 2. Проверка статус кода
    base_general.asserts.check_status_code(status_code=response.status_code, exp_status_code=200)

    # Шаг 3. Проверка тела ответа
    data = {
        '$.username': TestData.USERNAME[id_user],
        '$.email': TestData.JOB[id_user]
    }
    base_api.asserts.check_response_jsonpath(response=response.text, data=data)


@pytest.mark.xfail
@pytest.mark.parametrize('id_user',
                         [23])
def test_get_reqest_user_fail(base_api, base_general, id_user):
    """Нигативный тест.

    Шаг 1. Отправка запроса. Пример: GET https://reqres.in/api/users/2
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    """

    # Шаг 1. Запрос к апи
    response = base_api.api_v1.get_api_users(id_user=id_user)

    # Шаг 2. Проверка статус кода
    base_api.asserts.check_status_code(status_code=response.status_code, exp_status_code=200)



