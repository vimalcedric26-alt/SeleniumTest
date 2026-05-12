from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "user-name")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.NAME, "login-button")
        self.menu_button_input = (By.XPATH,"//button[text()='Open Menu']")
        self.logout_input = (By.XPATH,"//a[text()='Logout']")
        self.cart_icon = (By.CLASS_NAME,"shopping_cart_link")
        self.reset_input = (By.ID,"reset_sidebar_link")

    def navigate_url(self, url):
        self.driver.get(url)

    def user_name_details(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def password_details(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def login_click(self):
        self.driver.find_element(*self.login_button).click()

    def is_dashboard_loaded(self):
        return "inventory" in self.driver.current_url

    def click_menu_btn(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.menu_button_input)).click()

    def click_logout_btn(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.logout_input)).click()

    def get_page_title(self):
        return self.driver.title

    def is_cart_icon_visible(self):
        return self.driver.find_element(*self.cart_icon).is_displayed()

    def click_reset_btn(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.reset_input)).click()
