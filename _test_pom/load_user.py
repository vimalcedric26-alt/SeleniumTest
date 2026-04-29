from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_sauceDDTF:
    def test_login_excel(self):
        self.excel = Data.excel_file
        self.sheet = Data.sheet_number
