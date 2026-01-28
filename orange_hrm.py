import time
# from asyncio import wait_for
# from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from webdriver_manager.chrome.import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.ie.webdriver import WebDriver
#from webdriver_manager.drivers.firefox import GeckoDriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_choice_role = str(input("Enter role you would like to choose:"))
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,'username').send_keys('Admin')
driver.find_element(By.NAME,'password').send_keys('admin123')
driver.find_element(By.TAG_NAME,'button').click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Admin']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[1]").click()
time.sleep(4)

roles = driver.find_elements(By.XPATH,"//div[@class='oxd-select-option']")
for user_role in roles:
    role = user_role.text
    if role == user_choice_role:
        user_role.click()
        break
    elif role == user_choice_role:
        user_role.click()
        break
    else:
        continue

time.sleep(2)

driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys('user')
time.sleep(4)
element = driver.find_elements(By.XPATH, "//div[@class='oxd-autocomplete-option']")
for first_element in range(len(element)):
    element[first_element].click()
    break

time.sleep(4)
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]").send_keys('vimal')
driver.find_element(By.XPATH,"(//input[@type='password'])[1]").send_keys('123456@abc')
driver.find_element(By.XPATH,"(//div[@class='oxd-select-text-input'])[2]").click()
driver.find_element(By.XPATH,"//span[text()='Enabled']").click()
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]").send_keys('123456@abc')
driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
time.sleep(5)

wait = webdriver(driver,10)
message = wait.until(EC.visibility_of_element_located(By.XPATH,"//p[@class='oxd-text oxd-text--toast-title oxd-toast-content-text']"))
print(message.text)


driver.quit()

