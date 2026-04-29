import re
from playwright.sync_api import expect


class ClaimPage:
    def __init__(self, page):
        self.page = page

    def verify_claim_click(self):
        self.page.get_by_role("link", name="Claim").click()
        expect(self.page).to_have_url(re.compile("claim"))

    def initiate_claim_request(self):
        # Assign Claim button
        assign_btn = self.page.get_by_role("button", name="Assign Claim")
        expect(assign_btn).to_be_visible()
        assign_btn.click()

    def enter_claim_details(self):
        field = self.page.get_by_placeholder("Type for hints...")
        field.fill("a")
        self.page.wait_for_selector(".oxd-autocomplete-option")
        self.page.locator(".oxd-autocomplete-option").nth(1).click()

        # Dropdowns
        dropdowns = self.page.locator("div.oxd-select-text")

        dropdowns.nth(0).click()
        self.page.locator(".oxd-select-option").nth(1).click()

        dropdowns.nth(1).click()
        self.page.locator(".oxd-select-option").nth(1).click()

        remarks = self.page.locator("textarea")
        remarks.fill("Automated Claim Submission")

        # Create claim
        create_btn = self.page.get_by_role("button", name="Create")
        expect(create_btn).to_be_visible()
        create_btn.click(no_wait_after=True)

        self.page.wait_for_timeout(3000)

    def verify_claim_success_message(self):
        self.page.wait_for_timeout(3000)

        toast = self.page.locator(".oxd-toast")
        if toast.count() > 0:
            expect(toast).to_be_visible()
        else:
            error_msg = self.page.locator(".oxd-input-field-error-message")
            expect(error_msg).to_have_count(0)

    def verify_claim_history_present(self):
        # Navigate to My Claims
        self.page.get_by_role("link", name="My Claims").click()

        expect(self.page).to_have_url(re.compile("viewClaim"))

        search_btn = self.page.get_by_role("button", name="Search")
        expect(search_btn).to_be_visible()
        search_btn.click(no_wait_after=True)

        self.page.wait_for_timeout(3000)

        reset_btn = self.page.get_by_role("button", name="Reset")
        expect(reset_btn).to_be_visible()