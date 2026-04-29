import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://www.guvi.in/")

wait = WebDriverWait(driver, 10)
driver.find_element(By.ID, "login-btn").click()# Click Login button
# Enter Email
wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("")
# Enter Password
wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("")
# Click Login
wait.until(EC.element_to_be_clickable((By.ID,"login-btn"))).click()
time.sleep(4)

driver.save_screenshot("guvi1.png")
print(driver.title)
driver.quit()
