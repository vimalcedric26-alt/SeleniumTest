from playwright.sync_api import TimeoutError

class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def enter_text(self, locator, text):
        self.page.locator(locator).fill(text)


