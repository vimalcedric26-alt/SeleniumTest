import re
from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_input = page.get_by_role("button", name="Login")
        self.forgot_pwd_input = page.get_by_text("Forgot your password? ")

    def load(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.page.wait_for_load_state("domcontentloaded")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_input.click()

        # ---- CRITICAL JENKINS WAIT ----
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(4000)
        expect(self.page).to_have_url(re.compile("dashboard"), timeout=15000)
        expect(self.page.locator(".oxd-userdropdown-name")).to_be_visible(timeout=15000)

    def verify_login_success(self):
        expect(self.page).to_have_url(re.compile("dashboard"), timeout=15000)
        expect(self.page.locator(".oxd-userdropdown-name")).to_be_visible(timeout=15000)

    def verify_login_fields_present(self):
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.username_input).to_be_enabled()
        expect(self.password_input).to_be_enabled()

    def forgot_password_click(self):
        expect(self.forgot_pwd_input).to_be_visible()
        self.forgot_pwd_input.click()

    def verify_forgot_password_redirect(self):
        expect(self.page).to_have_url(re.compile("requestPasswordResetCode"), timeout=10000)

    def submit_reset_password(self, username):
        reset_input = self.page.get_by_placeholder("Username")
        reset_input.fill(username)

        reset_btn = self.page.get_by_role("button", name="Reset Password")
        expect(reset_btn).to_be_visible()
        reset_btn.click()
        self.page.wait_for_load_state("networkidle")