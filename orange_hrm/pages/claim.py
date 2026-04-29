import re
from playwright.sync_api import expect


class ClaimPage:
    def __init__(self, page):
        self.page = page

    def verify_claim_click(self):
        claim_menu = self.page.get_by_role("link", name="Claim")
        expect(claim_menu).to_be_visible(timeout=15000)
        claim_menu.click()

        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url(re.compile("claim"), timeout=15000)

    def initiate_claim_request(self):
        assign_btn = self.page.get_by_role("button", name="Assign Claim")
        expect(assign_btn).to_be_visible(timeout=15000)
        assign_btn.click()

        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)

    def enter_claim_details(self):
        field = self.page.get_by_placeholder("Type for hints...")
        field.fill("a")
        self.page.wait_for_selector(".oxd-autocomplete-option", timeout=15000)
        self.page.locator(".oxd-autocomplete-option").nth(1).click()

        dropdowns = self.page.locator("div.oxd-select-text")

        dropdowns.nth(0).click()
        self.page.locator(".oxd-select-option").nth(1).click()

        dropdowns.nth(1).click()
        self.page.locator(".oxd-select-option").nth(1).click()

        remarks = self.page.locator("textarea")
        remarks.fill("Automated Claim Submission")

        create_btn = self.page.get_by_role("button", name="Create")
        expect(create_btn).to_be_visible(timeout=15000)
        create_btn.click()

        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)

    def verify_claim_success_message(self):
        toast = self.page.locator(".oxd-toast")
        expect(toast).to_be_visible(timeout=15000)

    def verify_claim_history_present(self):
        my_claims = self.page.get_by_role("link", name="My Claims")
        expect(my_claims).to_be_visible(timeout=15000)
        my_claims.click()

        self.page.wait_for_load_state("networkidle")
        expect(self.page).to_have_url(re.compile("viewClaim"), timeout=15000)

        search_btn = self.page.get_by_role("button", name="Search")
        expect(search_btn).to_be_visible(timeout=15000)
        search_btn.click()

        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)

        reset_btn = self.page.get_by_role("button", name="Reset")
        expect(reset_btn).to_be_visible(timeout=15000)