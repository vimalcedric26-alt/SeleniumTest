import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/dropdown.html')
time.sleep(2)

# use of select tag for dropdown menus
# select = Select(driver.find_element(By.TAG_NAME,'select'))
# select.select_by_index(3)
# time.sleep(2)
# select.select_by_value('mercedes')

# Handling radio button with dynamic approach
# driver.find_element(By.XPATH,"//label[@for='demo-priority-normal']").click()

radio_btns = driver.find_elements(By.XPATH,"//label[contains(@for,'demo-priority')]")
for each_radio_btn in radio_btns: #[element1,element2,element3]
    each_radio_btn.click()
    time.sleep(2)

check_box = driver.find_elements(By.XPATH,"//label[contains(@for,'cb_')]")
for check_btn in check_box:
    check_btn.click()
    time.sleep(2)



