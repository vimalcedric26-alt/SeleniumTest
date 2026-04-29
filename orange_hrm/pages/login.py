import re
from playwright.sync_api import expect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_input = page.get_by_role("button", name="Login")
        self.leave_menu = page.get_by_role("link", name="Leave")
        self.forgot_pwd_input = page.get_by_text("Forgot your password? ")

    def load(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        self.page.locator('[name="username"]').fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def verify_login_success(self):
        expect(self.page).to_have_url(re.compile("dashboard"))
        expect(self.page.locator(".oxd-userdropdown-name")).to_be_visible()

    def verify_login_fields_present(self):
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()

        expect(self.username_input).to_be_enabled()
        expect(self.password_input).to_be_enabled()

    # def menu_items_present(self):
    #     # expect(self.leave_menu).to_be_visible()
    #     # expect(self.leave_menu).to_be_enabled()
    #
    #     self.leave_menu.click()

    def forgot_password_click(self):
        expect(self.forgot_pwd_input).to_be_visible()
        self.forgot_pwd_input.click()

    def verify_forgot_password_redirect(self):
        expect(self.page).to_have_url(re.compile("requestPasswordResetCode"))

    def submit_reset_password(self, username):
        reset_input = self.page.get_by_placeholder("Username")
        reset_input.fill(username)

        reset_btn = self.page.get_by_role("button", name="Reset Password")
        expect(reset_btn).to_be_visible()
        reset_btn.click(no_wait_after=True)






