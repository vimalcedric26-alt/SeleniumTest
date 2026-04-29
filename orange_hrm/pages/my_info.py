from playwright.sync_api import expect

class MyinfoPage:
    def __init__(self, page):
        self.page = page

    def verify_info_click(self):
        self.page.get_by_role("link", name="My Info").click()

    def verify_each_info_click(self):
        info_list = ["Personal Details", "Contact Details", "Emergency Contacts", "Dependents", "Immigration", "Job", "Salary", "Report-to", "Qualifications", "Memberships"]

        for info in info_list:
            item = self.page.get_by_role("link", name=info)
            expect(item).to_be_visible()
            expect(item).to_be_enabled()
            item.click()