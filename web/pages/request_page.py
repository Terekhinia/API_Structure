"""
Модуль содержит методы и локаторы для работы с начальной страницей
"""
from ..base.base_page import BasePage
from selenium.webdriver.common.by import By


class RequestPage(BasePage):

    SINGLE_USER = (By.XPATH, "//li[@data-id='users-single']")
    RESPONS = (By.XPATH, "//pre[@data-key = 'output-response']")
    CREATE_USER = (By.XPATH, "//li[@data-id='post']")
    PUT_USER = (By.XPATH, "//li[@data-id='put']")

    def click_button_get_single_user(self):
        """Клик по кнопке - GET 'SINGLE USER' """
        button_get_single_user = self.find_element(self.SINGLE_USER)
        button_get_single_user.click()

    def get_respons_single_user(self):
        """Получение текста Response в текстовом виде на GET запрос"""
        respons = self.find_element(self.RESPONS)
        respons_text = respons.text
        respons_text = respons_text.replace("\n", "").replace("    ", "")
        print(f'--{respons_text=}')
        return respons_text

    def click_button_post_user(self):
        """Клик по кнопке - POST 'CREATE' """
        button_post_user = self.find_element(self.CREATE_USER)
        button_post_user.click()

    def post_user(self):
        """Получение текста Response в текстовом виде на POST запрос"""
        respons = self.find_element(self.RESPONS)
        respons_text = respons.text
        respons_text = respons_text.replace("\n", "").replace("    ", "")
        print(f'--{respons_text=}')
        return respons_text

    def click_button_put_user(self):
        """Клик по кнопке - PUT 'APDATE' """
        button_put_user = self.find_element(self.PUT_USER)
        button_put_user.click()

    def put_user(self):
        """Получение текста Response в текстовом виде на PUT запрос"""
        respons = self.find_element(self.RESPONS)
        respons_text = respons.text
        respons_text = respons_text.replace("\n", "").replace("    ", "")
        print(f'--{respons_text=}')
        return respons_text
