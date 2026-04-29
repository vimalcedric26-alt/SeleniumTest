from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver
        self.username_loc = (By.ID,"useremail")
        self.password_loc = (By.ID,"password")
        self.login_loc = (By.ID,"loginBtn")
        self.profile_icon_loc = (By.XPATH, "//img[@class='gravatar']")
        self.logout_btn = (By.XPATH,"//a[contains(@id,'logout')]")

    def navigate_url(self,url):
        try:
            self.driver.get(url)
            return True
        except:raise Exception("Error navigating to login page ")

    def enter_username(self,username):
        self.driver.find_element(*self.username_loc).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_loc).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_loc).click()


    def profile_icon_click(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_icon_loc)).click()

    def log_out(self):
        self.driver.find_element(*self.logout_btn).click()


