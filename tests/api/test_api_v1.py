"""Пример позитивного теста через фикстуру"""
import pytest
import json


@pytest.mark.parametrize('id_user',
                         [2,
                          3])
def test_get_reqest_user(base, id_user):
    """Позитивный тест.

    Шаг 1. Отправка запроса. Пример: GET https://reqres.in/api/users/2
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    """

    # Шаг 1. Запрос к апи
    response = base.api_v1.get_api_users(id_user=id_user)

    # Шаг 2. Проверка статус кода
    base.asserts.check_status_code(status_code=response.status_code, exp_status_code=200)

    # Шаг 3. Проверка тела ответа
    first_name = base.testdata.FIRST_NAME[id_user]
    last_name = base.testdata.LAST_NAME[id_user]
    response_id = base.functions.jsonpath(response=response, value="data.id")
    response_last_name = base.functions.jsonpath(response=response, value="data.last_name")
    response_first_name = base.functions.jsonpath(response=response, value="data.first_name")
    base.asserts.check_id_users(response_id, id_user)
    base.asserts.check_name_users(response_last_name, last_name)
    base.asserts.check_name_users(response_first_name, first_name)


def test_post_create_user1(base):
    """Позитивный тест.

    Шаг 1. Отправка запроса. Пример: POST https://reqres.in/api/users
                                          Body {
                                               "name": "morpheus",
                                               "job": "leader"
                                                }
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    """
    number_user = 1

    # Шаг 1. Запрос к апи
    body = base.testdata.body_request(number_user)
    response = base.api_v1.post_api_created_users(data=body)

    # Шаг 2. Проверка статус кода
    base.asserts.check_status_code(status_code=response.status_code, exp_status_code=201)

    # Шаг 3. Проверка тела ответа
    username = base.testdata.USERNAME[number_user]
    email = base.testdata.JOB[number_user]
    response_username = base.functions.jsonpath(response=response, value="username")
    response_email = base.functions.jsonpath(response=response, value="email")
    base.asserts.check_name_users(response_username, username)
    base.asserts.check_name_users(response_email, email)


def test_put_chains_user1(base):
    """Позитивный тест.

    Шаг 1. Отправка запроса. Пример: PUT https://reqres.in/api/users
                                         Body {
                                              "name": "morpheus",
                                              "job": "zion resident"
                                              }
    Шаг 2. Проверка статус кода
    Шаг 3. Проверка тела ответа
    """
    number_user = 2
    # Шаг 1. Запрос к апи
    body = base.testdata.body_request(number_user)
    response = base.api_v1.put_api_chains_users(data=body, id=number_user)

    # Шаг 2. Проверка статус кода
    base.asserts.check_status_code(status_code=response.status_code, exp_status_code=200)

    # Шаг 3. Проверка тела ответа
    username = base.testdata.USERNAME[number_user]
    email = base.testdata.JOB[number_user]
    response_username = base.functions.jsonpath(response=response, value="username")
    response_email = base.functions.jsonpath(response=response, value="email")
    base.asserts.check_name_users(response_username, username)
    base.asserts.check_name_users(response_email, email)
