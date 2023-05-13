"""Модуль содержит все декораторы проекта"""
import pytest

from api.application import Application


@pytest.fixture(scope='session')
def base():
    """Декоратор по настройке только для API тестов"""
    return Application()
