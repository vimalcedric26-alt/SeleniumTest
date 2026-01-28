import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(4)

# find_element should always have unique element identifier/locator
driver.find_element(By.NAME,'username').send_keys('Admin')
driver.find_element(By.NAME,'password').send_keys('admin123')
driver.find_element(By.TAG_NAME,'button').click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Admin']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='ESS']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys('test')
time.sleep(4)
element = driver.find_elements(By.XPATH,"//div[@class='oxd-autocomplete-option']")
for first_element in range(len(element)):
    element[first_element].click()
    break
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys('test123')
driver.find_element(By.XPATH,"(//input[@type='password'])[1]").send_keys('test123')
driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[2]").click()
driver.find_element(By.XPATH,"//span[text()='Enabled']").click()
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]").send_keys('test123')
driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
time.sleep(2)

driver.quit()