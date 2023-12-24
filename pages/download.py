import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base import Base
import time

class Download(Base):
    def __init__(self,browser):
        super().__init__(browser)

    def scroll_down(self):
        time.sleep(10)
        self.teg = self.browser.find_element(By.LINK_TEXT,"Скачать СБИС")
        self.browser.execute_script("arguments[0].scrollIntoView(true);", self.teg)
        time.sleep(5)

    def click_dowland_sbis(self):
        self.teg.click()
        time.sleep(5)
    def click_sbis_plagin(self):
        self.teg_plagin = self.browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]").click()
        time.sleep(5)
        return self.browser.current_url

    def downloand_file(self):
        self.teg_downloand = self.browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div").click()
        time.sleep(5)
        file = os.listdir("D:/pytest/downloads")
        return file[0]
