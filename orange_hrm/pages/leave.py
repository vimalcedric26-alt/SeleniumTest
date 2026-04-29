import re
from playwright.sync_api import expect


class LeavePage:
    def __init__(self, page):
        self.page = page

    def verify_leave_click(self):
        leave_menu = self.page.get_by_role("link", name="Leave")
        expect(leave_menu).to_be_visible(timeout=15000)
        leave_menu.click()

        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url(re.compile("leave"), timeout=15000)

    def verify_assign_leave(self):
        assign_leave = self.page.get_by_role("link", name="Assign Leave")
        expect(assign_leave).to_be_visible(timeout=15000)
        assign_leave.click()

        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def verify_assign_leave_details(self):
        field = self.page.get_by_placeholder("Type for hints...")
        field.fill("a")
        self.page.wait_for_selector(".oxd-autocomplete-option", timeout=15000)
        self.page.locator(".oxd-autocomplete-option").nth(1).click()

        dropdown = self.page.locator("div.oxd-select-text").first
        dropdown.click()
        self.page.locator(".oxd-select-option").nth(1).click()

        date_field = self.page.locator("input[placeholder='yyyy-mm-dd']").first
        date_field.fill("2026-05-30")

        self.page.locator("textarea").fill("My Leave Assignment")

        self.page.get_by_role("button", name="Assign").click()

        ok_btn = self.page.get_by_role("button", name="Ok")
        expect(ok_btn).to_be_visible(timeout=10000)
        ok_btn.click()

        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)

    def verify_leave_success_message(self):
        toast = self.page.locator(".oxd-toast")
        expect(toast).to_be_visible(timeout=15000)

    def verify_leave_record_present(self):
        leave_list = self.page.get_by_role("link", name="Leave List")
        expect(leave_list).to_be_visible(timeout=15000)
        leave_list.click()

        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url(re.compile("viewLeaveList"), timeout=15000)

        search_btn = self.page.get_by_role("button", name="Search")
        expect(search_btn).to_be_visible(timeout=15000)
        search_btn.click()

        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)

        reset_btn = self.page.get_by_role("button", name="Reset")
        expect(reset_btn).to_be_visible(timeout=15000)

        error_popup = self.page.locator(".oxd-toast--error")
        expect(error_popup).to_have_count(0)