import time
import logging
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовый класс для работы с основными методами браузера и элементами"""

    def __init__(self, browser: EventFiringWebDriver, timeout: int = 10):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, timeout)
        self.browser.implicitly_wait(timeout)

    def find_element(self, locator) -> WebElement:
        return self.browser.find_element(by=locator[0], value=locator[1])

    def find_elements(self, locator) -> list[WebElement]:
        return self.browser.find_elements(by=locator[0], value=locator[1])

    def open(self, url):
        """Открыть страницу"""
        self.browser.get(url=url)

    def click_button(self, locator):
        """Клик по кнопке запроса"""
        button_get_single_user = self.find_element(locator)
        button_get_single_user.click()

    def respons(self, locator):
        """Получение текста Response в текстовом виде"""
        WebDriverWait(self.browser, 5).until_not(EC.element_attribute_to_include(locator, 'hidden'))
        respons = self.find_element(locator)
        respons_text = respons.text
        respons_text = respons_text.replace("\n", "").replace("    ", "")
        print(f'--{respons_text=}')
        return respons_text

    # def custom_wait(self, respons):
    #     for i in range(3):
    #         try:
    #             if respons.text != '':
    #                 break
    #         except: pass
    #         time.sleep(1)
    #     else:
    #         self.browser.quit()
    #         logging.info(print('Поле ответа пустое'))


