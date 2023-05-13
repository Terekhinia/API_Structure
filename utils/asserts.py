"""Модуль с шагами по проверке"""


class AssertApi:
    """Класс проверок для API"""

    @staticmethod
    def check_status_code(status_code, exp_status_code):
        """Метод проверки статус кода.

        Args:
            status_code: полученный из тела ответа статус код
            exp_status_code: ожидаемый статус код
        """
        # todo добавить шаг с allure или с логированием

        msg = f'Статус код ответа "{status_code}" отличен от "{exp_status_code}"'
        assert status_code == exp_status_code, msg


    @staticmethod
    def check_id_users(response_id, exp_id):
        """Метод проверки id юзера

        Args:
            response_id: полученный из тела ответа id
            exp_id: ожидаемый id
        """

        msg = f'полученный id - "{response_id}" отличен от "{exp_id}"'
        assert response_id == exp_id, msg

    @staticmethod
    def check_name_users(response_name, exp_name):
        """Метод проверки name юзера

        Args:
            response_name: полученный из тела ответа name
            exp_name: ожидаемый name
        """

        msg = f'полученный name - "{response_name}" отличен от "{exp_name}"'
        assert response_name == exp_name, msg