from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ZenPortalLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # self.login_popup_btn = (By.ID, "loginBtn")
        self.username_loc = (By.ID,"useremail")
        self.password_loc = (By.ID, "password")
        self.login_btn_loc = (By.ID,"loginBtn")
        self.profile_icon = (By.XPATH, "//img[@class='gravatar']")

        self.logout_loc = (By.XPATH,"//a[contains(@id,'logout')]")

    def navigate_url(self):
        self.driver.get("https://classify.zenclass.in/")

    def login(self):
        # self.wait.until(EC.element_to_be_clickable(self.login_popup_btn)).click()
        # time.sleep(5)

        self.driver.find_element(*self.username_loc).send_keys("vimalcedric26@gmail.com")
        self.driver.find_element(*self.password_loc).send_keys("Cassy@091124")
        time.sleep(5)

        self.wait.until(EC.visibility_of_element_located(self.login_btn_loc)).click()

    def open_dropdown(self):

        self.wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def logout(self):

            self.wait.until(EC.visibility_of_element_located(self.logout_loc)).click()

            return self.driver.title
