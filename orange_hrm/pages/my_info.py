from playwright.sync_api import expect

class MyinfoPage:
    def __init__(self, page):
        self.page = page

    def verify_info_click(self):
        myinfo_menu = self.page.get_by_role("link", name="My Info")
        expect(myinfo_menu).to_be_visible(timeout=15000)
        myinfo_menu.click()

        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(3000)

    def verify_each_info_click(self):
        info_list = [
            "Personal Details",
            "Contact Details",
            "Emergency Contacts",
            "Dependents",
            "Immigration",
            "Job",
            "Salary",
            "Report-to",
            "Qualifications",
            "Memberships"
        ]

        for info in info_list:
            item = self.page.get_by_role("link", name=info)
            expect(item).to_be_visible(timeout=15000)
            expect(item).to_be_enabled(timeout=15000)
            item.click()
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1500)