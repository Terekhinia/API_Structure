"""Модуль содержит тестовые данные"""


class TestData:

    # список имен и фамилий тестовых юзеров
    LAST_NAME = {2: "Weaver", 3: "Wong"}
    FIRST_NAME = {2: "Janet", 3: "Emma"}


    # список тестовых данных для создания/редактирования юзера
    USERNAME = {1: "morpheus", 2: "morpheus"}
    JOB = {1: "leader", 2: "zion resident"}

    NUMBER_GET_SINGLE_USER = 2
    NUMBER_UPDATE_USER = 2
    NUMBER_CREATE_USER = 1

    # тело запроса для создания нового юзера
    def body_request(self, id_user):
        body = {"username": self.USERNAME[id_user], "email": self.JOB[id_user]}
        return body









