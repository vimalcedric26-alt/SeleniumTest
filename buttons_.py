import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
driver.get("https://automationtesting.co.uk/buttons.html")

action = ActionChains(driver)
move_to_btn = driver.find_element(By.ID,"btn_three")
action.move_to_element(move_to_btn).click().perform()
time.sleep(2)
driver._switch_to.alert.accept()

print(driver.find_element(By.ID,"btn_four").is_enabled())