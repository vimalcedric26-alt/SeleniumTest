import time
from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.add_argument('__private')
option.add_argument('__headless')

driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()),options=option)
driver.get('https://www.automationtesting.co.uk/index.html')
abs_xpath_elements = '/html/body/div/div/div/section/div/div/article[3]/div[2]/h3/a'
lst_of_course = driver.find_elements(By.XPATH,'abs_xpath_elements')
for each_course in lst_of_course:
    print(each_course.text)
driver.quit()

