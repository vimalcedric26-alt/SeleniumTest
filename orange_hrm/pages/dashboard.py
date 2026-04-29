import re
import time
from playwright.sync_api import expect


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def verify_menu_items_click(self):
        menu_list = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]
        self.page.wait_for_selector(".oxd-sidepanel-body", timeout=20000)

        for menu in menu_list:
            item = self.page.get_by_role("link", name=menu)
            expect(item).to_be_visible(timeout=15000)
            expect(item).to_be_enabled(timeout=15000)
            item.click()
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(2000)

    def verify_admin_adding_new_user(self):
        admin_menu = self.page.get_by_role("link", name="Admin")
        expect(admin_menu).to_be_visible(timeout=15000)
        admin_menu.click()

        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url(re.compile("admin"), timeout=15000)

        add_btn = self.page.get_by_role("button", name="Add")
        expect(add_btn).to_be_visible(timeout=15000)
        add_btn.click()

        self.page.wait_for_load_state("networkidle")

    def adding_user_details(self):
        username = "vimal" + str(int(time.time()))
        password = "Admin@123"

        dropdowns = self.page.locator("div.oxd-select-text")

        dropdowns.nth(0).click()
        self.page.locator(".oxd-select-option", has_text="Admin").click()

        field = self.page.get_by_placeholder("Type for hints...")
        field.fill("a")
        self.page.wait_for_selector(".oxd-autocomplete-option", timeout=15000)
        self.page.locator(".oxd-autocomplete-option").nth(1).click()

        dropdowns.nth(1).click()
        self.page.locator(".oxd-select-option", has_text="Enabled").click()

        self.page.get_by_role("textbox").nth(2).fill(username)
        self.page.get_by_role("textbox").nth(3).fill(password)
        self.page.get_by_role("textbox").nth(4).fill(password)

        self.page.get_by_role("button", name="Save").click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(4000)

        return username

    def search_and_verify_user(self, username):
        admin_menu = self.page.get_by_role("link", name="Admin")
        expect(admin_menu).to_be_visible(timeout=15000)
        admin_menu.click()

        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url(re.compile("admin"), timeout=15000)

        search_box = self.page.locator('input.oxd-input').nth(1)
        search_box.fill(username)

        self.page.get_by_role("button", name="Search").click()
        self.page.wait_for_selector(".oxd-table-body", timeout=15000)

        user_cell = self.page.locator(".oxd-table-cell", has_text=username)
        expect(user_cell).to_be_visible(timeout=15000)

    def logout(self):
        dropdown = self.page.locator(".oxd-userdropdown-tab")
        expect(dropdown).to_be_visible(timeout=15000)
        dropdown.click()

        logout_btn = self.page.get_by_role("menuitem", name="Logout")
        expect(logout_btn).to_be_visible(timeout=15000)
        logout_btn.click()

        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url(re.compile("login"), timeout=15000)