import re
import time
from playwright.sync_api import expect


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def verify_menu_items_click(self):
        menu_list = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]

        for menu in menu_list:
            item = self.page.get_by_role("link", name=menu)
            expect(item).to_be_visible()
            expect(item).to_be_enabled()
            item.click()

    def verify_admin_adding_new_user(self):
        self.page.get_by_role("link", name="Admin").click()
        expect(self.page).to_have_url(re.compile("admin"))
        self.page.get_by_role("button", name="Add").click()

    def adding_user_details(self):
        username = "vimal" + str(int(time.time()))
        password = "Admin@123"

        dropdowns = self.page.locator("div.oxd-select-text")

        # User Role
        dropdowns.nth(0).click()
        self.page.locator(".oxd-select-option", has_text="Admin").click()

        # Employee Name
        field = self.page.get_by_placeholder("Type for hints...")
        field.fill("a")
        self.page.wait_for_selector(".oxd-autocomplete-option")
        self.page.locator(".oxd-autocomplete-option").nth(1).click()

        # Status
        dropdowns.nth(1).click()
        self.page.locator(".oxd-select-option", has_text="Enabled").click()

        # Credentials
        self.page.get_by_role("textbox").nth(2).fill(username)
        self.page.get_by_role("textbox").nth(3).fill(password)
        self.page.get_by_role("textbox").nth(4).fill(password)

        self.page.get_by_role("button", name="Save").click()

        self.page.wait_for_timeout(3000)

        return username

    def search_and_verify_user(self, username):
        self.page.get_by_role("link", name="Admin").click()
        expect(self.page).to_have_url(re.compile("admin"))

        search_box = self.page.locator('input.oxd-input').nth(1)
        search_box.fill(username)

        self.page.get_by_role("button", name="Search").click()

        self.page.wait_for_selector(".oxd-table-body")

        user_cell = self.page.locator(".oxd-table-cell", has_text=username)
        expect(user_cell).to_be_visible()

    def logout(self):
        dropdown = self.page.locator(".oxd-userdropdown-tab")
        expect(dropdown).to_be_visible()
        dropdown.click()

        logout_btn = self.page.get_by_role("menuitem", name="Logout")
        expect(logout_btn).to_be_visible()
        logout_btn.click()

        expect(self.page).to_have_url(re.compile("login"))

    def verify_forgot_pwd(self):
        self.page.get_by_role("text","Forgot your password? ").click()