import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/datepicker.html')
driver.maximize_window()

driver.find_elements(By.ID,'Select Date..').click()
select_date = driver.find_elements(By.XPATH,"//div[@class='dayContainer']/span")
for each_date in select_date:
    if each_date.text == '20':
        driver.find_element(By.TAG_NAME,'body').click()
           break: