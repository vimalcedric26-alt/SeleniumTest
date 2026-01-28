import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from webdriver_manager.chrome.import ChromeDriverManager
from selenium.webdriver.common.by import By
#from webdriver_manager.drivers.firefox import GeckoDriver
from webdriver_manager.firefox import GeckoDriverManager



driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.ID,'firstName').send_keys("Vimal")
driver.find_element(By.ID,'lastName').send_keys("cedric")
driver.find_element(By.ID,'userEmail').send_keys("demo@email.com")
driver.find_element(By.ID,'userNumber').send_keys("123456789")
driver.find_element(By.ID,'dateOfBirthInput').send_keys("1980-01-01")
driver.find_element(By.ID,'subjectsContainer').click()
time.sleep(3)
print(driver.title)
driver.save_screenshot("Demo.png")
driver.quit()