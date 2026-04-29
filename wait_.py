import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/loader.html')
driver.maximize_window()

driver.implicitly_wait(10)
print(driver.find_element(By.ID,'content').text)
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.ID,'loaderBtn'))).click()