from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username = "#txtUsername"
        self.password = "#txtPassword"
        self.login_btn = "#btnLogin"

    def login(self, user, pwd):
        self.enter_text(self.username, user)
        self.enter_text(self.password, pwd)
        self.click(self.login_btn)