from orange_hrm.pages.login import LoginPage
from orange_hrm.pages.dashboard import DashboardPage
from orange_hrm.pages.my_info import MyinfoPage
from orange_hrm.pages.leave import LeavePage
from orange_hrm.pages.claim import ClaimPage

class TestLogin:

    def test_valid_login(self, page):
        login_page = LoginPage(page)

        login_page.load()
        login_page.login("Admin", "admin123")
        login_page.verify_login_success()


    def test_login_fields_visibility(self,page):
        login_page = LoginPage(page)

        login_page.load()
        login_page.verify_login_fields_present()

    def test_menu_items(self,page):
        login = LoginPage(page)
        dashboard = DashboardPage(page)

        login.load()
        login.login("Admin", "admin123")

        dashboard.verify_menu_items_click()

    def test_admin_page(self,page):
        login = LoginPage(page)
        dashboard = DashboardPage(page)

        login.load()
        login.login("Admin", "admin123")

        dashboard.verify_admin_adding_new_user()
        dashboard.adding_user_details()

        dashboard.logout()

    def test_add_and_verify_new_user(self,page):
        login = LoginPage(page)
        dashboard = DashboardPage(page)

        login.load()
        login.login("Admin", "admin123")
        login.verify_login_success()

        dashboard.verify_admin_adding_new_user()
        created_username = dashboard.adding_user_details()

        dashboard.search_and_verify_user(created_username)

    def test_forgot_pwd_page(self,page):
        login = LoginPage(page)
        login.load()
        login.forgot_password_click()
        login.verify_forgot_password_redirect()
        login.submit_reset_password("Admin")

    def test_info_page(self,page):
        login = LoginPage(page)

        myinfo = MyinfoPage(page)

        login.load()
        login.login("Admin", "admin123")
        myinfo.verify_info_click()
        myinfo.verify_each_info_click()

    def test_leave_page(self,page):
        login = LoginPage(page)
        leave = LeavePage(page)

        login.load()
        login.login("Admin", "admin123")
        leave.verify_leave_click()
        leave.verify_assign_leave()

        leave.verify_assign_leave_details()
        leave.verify_leave_success_message()
        leave.verify_leave_record_present()

    def test_claim_request(self, page):
        login = LoginPage(page)
        claim = ClaimPage(page)

        login.load()
        login.login("Admin", "admin123")

        claim.verify_claim_click()
        claim.initiate_claim_request()
        claim.enter_claim_details()

        claim.verify_claim_success_message()
        claim.verify_claim_history_present()


