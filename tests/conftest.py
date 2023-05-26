import pytest
from selenium import webdriver
from api.application import Application
from utils.utils import Utils


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path='web/webdrivers/chromedriver.exe')
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope='session')
def base_general():
    """Декоратор для работы с общими данными и функциями для вэб и апи"""
    return Utils()


@pytest.fixture(scope='session')
def base_api():
    """Декоратор по настройке только для API тестов"""
    return Application()

