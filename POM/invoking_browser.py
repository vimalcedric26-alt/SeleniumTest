
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class Browser:
    def invoke_browser(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.implicitly_wait(10)
        return driver
        # yield driver
        # driver.quit()
