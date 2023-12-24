from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class Base:
    def __init__(self,browser):
        self.browser = browser

    def get_page(self):
        self.browser.get('https://sbis.ru')

