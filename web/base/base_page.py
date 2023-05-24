from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


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

