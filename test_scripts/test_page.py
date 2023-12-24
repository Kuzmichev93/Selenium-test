import allure

from pages.page import Page
from conftest import *
import pytest
"""Второй сценарий"""

@allure.feature("Второй сценарий")
@allure.story("Проверка на соответствие региона")
def test_region(browser):
    browser = Page(browser)
    browser.get_page()
    with allure.step("Переход в раздел 'Контакты'"):
        browser.click_contact()
    with allure.step("Сохранение названия региона"):
        assert browser.get_teg_region().text == 'Владимирская обл.'

@allure.feature("Второй сценарий")
@allure.story("Проверка изменения региона, title, url и филиала")
def test_update_region(browser):
    browser = Page(browser)
    browser.get_page()
    with allure.step("Переход в раздел 'Контакты'"):
        browser.click_contact()
    with allure.step("Клик по региону"):
        browser.click_region()
    with allure.step("Изменение региона на 'Камчатский край'"):
        browser.click_update_region()

    assert browser.get_teg_region().text == 'Камчатский край'
    assert browser.get_title() == "СБИС Контакты — Камчатский край"
    assert browser.get_url() == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
    assert browser.get_teg_partner() == "Петропавловск-Камчатский"