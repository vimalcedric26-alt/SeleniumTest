import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get('https://automationtesting.co.uk/actions.html')

action = ActionChains(driver)
time.sleep(2)
source = driver.find_element(By.XPATH,"//div[@class='droptarget'][1]")
target = driver.find_element(By.XPATH,"//div[@class='droptarget'][2]")
action.drag_and_drop(source=source,target=target).perform()
time.sleep(2)

double_click_element = driver.find_element(By.ID,"doubleClickArea")
action.double_click(double_click_element).perform()
time.sleep(2)

Holding_element = driver.find_element(By.ID,"holdDown")
action.click_and_hold(Holding_element).perform()
time.sleep(2)

Hold_shift_element = driver.find_element(By.XPATH,"//p[text()='Hold Shift & Click Here']")
action.click_and_hold(Hold_shift_element).perform()
time.sleep(2)

