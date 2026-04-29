from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.login_loc = (By.ID,'login-btn')
        self.email_loc = (By.ID,"email")
        self.password_loc = (By.ID,"password")
        self.login_btn = (By.ID,'login-btn')
        self.invalid_error = (By.XPATH,'//div[@class="invalid-feedback is-invalid"]')
        #menu_items_locators
        self.live_class_loc = (By.XPATH,'//p[text()="LIVE Classes"]')
        self.course_loc = (By.XPATH,'//p[text()="Courses"]')
        self.practice_loc = (By.XPATH, '//p[text()="Practice"]')
        self.resource_loc = (By.XPATH, '//p[text()="Resources"]')
        self.our_product_loc = (By.XPATH, '//p[text()="Our Products"]')
        #Logout locator
        self.profile_icon = (By.XPATH,'//img[@class ="rounded-full gravatar w-8 h-8"]')
        self.logout_loc = (By.XPATH,'//p[text()="Sign Out"]')
        #dobby_locator
        self.dobby_loc = (By.XPATH,'//span[@role="button"]')

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_loc)).click()

    def enter_user_details(self,email,password):
        self.wait.until(EC.visibility_of_element_located(self.email_loc)).send_keys(email)
        self.driver.find_element(*self.password_loc).send_keys(password)

    def submit_login(self):
        self.wait.until(EC.visibility_of_element_located(self.login_btn)).click()

    def invalid_error_display(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.invalid_error))
            return element
        except:
            return None

    def menu_items(self):
        self.wait.until(EC.presence_of_element_located(self.live_class_loc)).click()
        self.wait.until(EC.presence_of_element_located(self.course_loc)).click()
        self.wait.until(EC.presence_of_element_located(self.practice_loc)).click()
        self.wait.until(EC.presence_of_element_located(self.resource_loc)).click()
        self.wait.until(EC.presence_of_element_located(self.our_product_loc)).click()

    def click_dobby(self):
        self.wait.until(EC.element_to_be_clickable(self.dobby_loc)).click()

    def open_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def log_out_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.logout_loc)).click()