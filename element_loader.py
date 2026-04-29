import time
from xml.dom.xmlbuilder import Options

from requests import options
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

option = Options()
option.add_argument('__private')
option.add_argument('--headless')
driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()),options=option)
driver.get('https://automationtesting.co.uk/loader.html')

wait = WebDriverWait(driver,10)
print(wait.until(expected_conditions.visibility_of_element_located((By.ID,'loaderBtn'))).text)
driver.quit()


