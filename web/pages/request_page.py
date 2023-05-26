"""
Модуль содержит методы и локаторы для работы с начальной страницей
"""
from ..base.base_page import BasePage
from selenium.webdriver.common.by import By


class RequestPage(BasePage):

    SINGLE_USER = (By.XPATH, "//li[@data-id='users-single']")
    RESPONS = (By.XPATH, "//pre[@data-key = 'output-response']")
    CREATE_USER = (By.XPATH, "//li[@data-id='post']")
    UPDATE_USER = (By.XPATH, "//li[@data-id='put']")
