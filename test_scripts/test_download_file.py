from pages.download import  Download
from conftest import *
import pytest
import allure

"""Третий сценарий"""

@allure.feature("Третий сценарий")
@allure.story("Переход на страницу СБИС Плагин")
def test_checking_the_page(browser):
    browser = Download(browser)
    browser.get_page()
    with allure.step("Скролл до тега 'Скачать СБИС'"):
        browser.scroll_down()
    with allure.step("Клик по тегу 'Скачать СБИС'"):
        browser.click_dowland_sbis()

    assert browser.click_sbis_plagin()== "https://sbis.ru/download?tab=plugin&innerTab=default"

@allure.feature("Третий сценарий")
@allure.story("Загрузка файла")
def test_download_file(dowland):
    browser = Download(dowland)
    with allure.step("Загрузка файла"):

        assert browser.downloand_file() != ""
    #with allure.step("Проверка размера загруженного файла"):
    #    size = os.path.getsize("/test_scripts/downloads/Не подтвержден 263314.crdownload")
    #    assert confertor(size) == "7.02"

@allure.feature("Третий сценарий")
@allure.story("Проверка размера загруженного файла")
def test_check_size_file(download_size):
    with allure.step("Функция convertor принимает на вход бит, и возвращает MB"):
        assert convertor(download_size) == "7.02"
