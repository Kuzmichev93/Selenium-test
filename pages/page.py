import time

from selenium.webdriver.common.by import By

from pages.base import Base


class Page(Base):
    def __init__(self,browser):
        super().__init__(browser)


    def click_contact(self):
        self.browser.find_element(By.LINK_TEXT,"Контакты").click()
        time.sleep(5)

    def get_teg_region(self):
        return self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span")

    def click_region(self):
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span").click()
        time.sleep(5)
    def click_update_region(self):
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span").click()
        time.sleep(5)

    def get_title(self):
        return self.browser.title

    def get_url(self):
        return self.browser.current_url

    def get_teg_partner(self):
        return self.browser.find_element(By.ID,"city-id-2").text