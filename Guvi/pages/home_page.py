from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class GuviPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_btn = (By.XPATH, '//button[text()="Login"]')
        self.signup_btn = (By.XPATH, '//button[text()="Sign up"]')

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def is_login_button_visible(self, wait):
        return wait.until(EC.element_to_be_clickable(self.login_btn))

    def is_signup_button_visible(self, wait):
        return wait.until(EC.element_to_be_clickable(self.signup_btn))

    def check_in_signup_button(self,wait):
        return wait.until(EC.element_to_be_clickable(self.signup_btn)).click()