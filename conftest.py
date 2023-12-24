import os
import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By



@pytest.fixture()
def browser():
    chrome_br = webdriver.Chrome()
    chrome_br.implicitly_wait(10)
    return chrome_br


@pytest.fixture()
def page_tensor():
    chrome_br = webdriver.Chrome()
    chrome_br.implicitly_wait(10)
    chrome_br.get("https://tensor.ru/")
    return chrome_br

def page_about():
    chrome_br = webdriver.Chrome()
    chrome_br.implicitly_wait(10)
    chrome_br.get("https://tensor.ru/about")
    time.sleep(5)
    list_size = []
    size = chrome_br.find_elements(By.XPATH,"//div[@class='tensor_ru-About__block3-image-wrapper']/img")
    for k in size:
        list_size.append(pytest.param((k.size['height'],k.size['width']),id=k.tag_name))

    return list_size

@pytest.fixture()
def dowland():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory":f"{os.getcwd()}\downloads"}
    options.add_experimental_option("prefs",prefs)
    chrome_br = webdriver.Chrome(options=options)
    chrome_br.implicitly_wait(10)
    chrome_br.get("https://sbis.ru/download?tab=plugin&innerTab=default")
    return chrome_br

@pytest.fixture()
def download_size():
    file = os.listdir("D:/pytest/downloads")
    size = os.path.getsize("D:/pytest/downloads/"+file[0])
    return size

def convertor(bytes):
    a = 1
    b = 1048576
    result = (a/b)*bytes
    return format(result,'.2f')