from playwright.sync_api import sync_playwright, expect

class LoginPage:
    def __init__(self,page):
        self.email = page.get_by_role("textbox", name="Email")
        self.password = page.get_by_role("textbox", name="Password")
        self.signin_btn = page.get_by_role("button", name="Sign in")
        self.close_popup = page.get_by_role("button", name="Close popup")
        self.profile_icon = page.locator(".profile-click-icon-div")
        self.logout_btn = page.get_by_text("Log out")

    def login(self,username,password):
        self.email.fill(username)
        self.password.fill(password)
        self.signin_btn.click()

    def close_popup_if_present(self):
            expect(self.close_popup).to_be_visible(timeout=5000)
            self.close_popup.click()

    def log_out(self):
        expect(self.profile_icon).to_be_visible()
        self.profile_icon.click()
        self.logout_btn.click()