from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from conftest import *
from pages.base import *
from pages.teg import Teg
import time
import allure

"""Первый сценарий"""

@allure.feature("Первый сценарий")
@allure.story("Клик по баннеру Тензор и поиск блока 'Сила в людях'")
def test_find_teg(browser):

    browser = Teg(browser)
    browser.get_page()
    with allure.step("Клик по Тензор"):
        browser.click_contact_tensor()
    with allure.step("Поиск блока 'Cила в людях'"):
        result = browser.find_on_page_teg()
        assert result.text == "Сила в людях"

@allure.feature("Первый сценарий")
@allure.story("Проверка перехода на страницу")
def test_get_page(page_tensor):
    browser = Teg(page_tensor)
    with allure.step("Переход на страницу"):
        url = browser.click_about()
        assert url == "https://tensor.ru/about"


@allure.feature("Первый сценарий")
@allure.story("Поиск изображений, проверка высоты и ширины найденных изображений")
@pytest.mark.parametrize('arg',page_about())
def test_image(arg):

    assert arg == (192,270)

