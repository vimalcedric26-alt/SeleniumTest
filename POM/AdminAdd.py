from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager




class AdminAdd:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def __init__(self):
        self.AdminAdd_loc = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")

    def AdminAdd(self):
        self.driver.find_element(*self.AdminAdd_loc).click()

