import time

from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

from element_loader import option

option = Options()
option.add_argument('__private')
option.add_argument('__headless')

driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()),options=option)
driver.get('https://automationtesting.co.uk/tables.html')
time.sleep(2)

tables = driver.find_elements(By.XPATH,"//table[@class='sortable']/tbody/tr/td")
for table in tables:
    print(table.text)

time.sleep(2)


