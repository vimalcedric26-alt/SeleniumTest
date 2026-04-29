from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


        self.signup_loc = (By.XPATH, '//button[text()="Sign up"]')
        self.name_loc = (By.ID, 'name')
        self.email_loc = (By.ID, 'email')
        self.password_loc = (By.ID, 'password')
        self.mobile_input = (By.XPATH, '//input[@id="mobileNumber"]')

        self.signup_btn =(By.ID,'signup-btn')

    def click_signup_button(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_loc)).click()

    def enter_signup_details(self, username, email, password):
        self.wait.until(EC.visibility_of_element_located(self.name_loc)).send_keys(username)
        self.driver.find_element(*self.email_loc).send_keys(email)
        self.driver.find_element(*self.password_loc).send_keys(password)

    def enter_mobile(self, mobile):
        self.wait.until(EC.visibility_of_element_located(self.mobile_input)).send_keys(mobile)
        self.wait.until(EC.visibility_of_element_located(self.signup_btn)).click()




