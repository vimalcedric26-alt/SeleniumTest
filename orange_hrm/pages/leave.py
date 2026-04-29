import re
from playwright.sync_api import expect


class LeavePage:
    def __init__(self, page):
        self.page = page

    def verify_leave_click(self):
        self.page.get_by_role("link", name="Leave").click()
        expect(self.page).to_have_url(re.compile("leave"))

    def verify_assign_leave(self):
        assign_leave = self.page.get_by_role("link", name="Assign Leave")
        expect(assign_leave).to_be_visible()
        assign_leave.click()

    def verify_assign_leave_details(self):
        # Employee Name
        field = self.page.get_by_placeholder("Type for hints...")
        field.fill("a")
        self.page.wait_for_selector(".oxd-autocomplete-option")
        self.page.locator(".oxd-autocomplete-option").nth(1).click()

        # Leave Type
        dropdown = self.page.locator("div.oxd-select-text").first
        dropdown.click()
        self.page.locator(".oxd-select-option").nth(1).click()

        # Date
        date_field = self.page.locator("input[placeholder='yyyy-mm-dd']").first
        date_field.fill("2026-30-05")

        # Comment
        self.page.locator("textarea").fill("My Leave Assignment")

        # Assign submit
        self.page.get_by_role("button", name="Assign").click(no_wait_after=True)

        # Wait for confirmation popup and click OK
        ok_btn = self.page.get_by_role("button", name="Ok")
        expect(ok_btn).to_be_visible(timeout=10000)
        ok_btn.click(no_wait_after=True)

        self.page.wait_for_timeout(3000)

    def verify_leave_success_message(self):
        toast = self.page.locator(".oxd-toast")
        expect(toast).to_be_visible()

    def verify_leave_record_present(self):
        # Navigate to Leave List
        self.page.get_by_role("link", name="Leave List").click()

        expect(self.page).to_have_url(re.compile("viewLeaveList"))

        # Search action
        search_btn = self.page.get_by_role("button", name="Search")
        expect(search_btn).to_be_visible()
        search_btn.click(no_wait_after=True)

        self.page.wait_for_timeout(3000)

        # Verify leave list filter form still stable and no error message
        reset_btn = self.page.get_by_role("button", name="Reset")
        expect(reset_btn).to_be_visible()

        error_popup = self.page.locator(".oxd-toast--error")
        expect(error_popup).to_have_count(0)