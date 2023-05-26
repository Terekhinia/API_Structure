from utils.testdata import TestData
from utils.asserts import AssertApi


class Utils:
    """Класс с подключением всех библиотек """
    def __init__(self):
        self.asserts = AssertApi()
        self.testdata = TestData()

