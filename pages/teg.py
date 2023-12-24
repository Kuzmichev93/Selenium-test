from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base import Base
import time

class Teg(Base):
    def __init__(self,browser):
        super().__init__(browser)

    def click_contact_tensor(self):
        self.browser.find_element(By.LINK_TEXT,"Контакты").click()
        self.browser.find_element(By.XPATH,"//a[@href='https://tensor.ru/']").click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        time.sleep(5)

    def click_contact(self):
        self.browser.find_element(By.LINK_TEXT,"Контакты").click()
        time.sleep(5)
    def find_on_page_teg(self):
        return self.browser.find_element(By.XPATH,"//*[contains(text(), 'Сила в людях')]")

    def click_about(self):
        self.browser.find_element(By.XPATH,"//a[@href='/about']").click()
        time.sleep(5)
        return self.browser.current_url

    def list_size_image(self):
        time.sleep(5)
        list_size = []
        size = self.browser.find_elements(By.XPATH,"//div[@class='tensor_ru-About__block3-image-wrapper']/img")
        for k in size:
            list_size.append((k.size["height"],k.size["width"]))

        return list_size