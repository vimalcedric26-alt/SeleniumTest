from Guvi.pages.login import LoginPage
from Guvi.user_data import ExcelData
import pytest

excel = ExcelData(
        "Guvi/testdata/Guvi_excel.xlsx",
        "user_data"
    )
test_data = excel.get_data()

class TestLogin:
    @pytest.mark.parametrize("email,password,expected", test_data)
    def test_login_excel(self,setup, email, password, expected):
        driver, wait = setup
        page = LoginPage(driver)

        page.click_login()
        page.enter_user_details(email, password)
        page.submit_login()
        expected_url = "https://www.guvi.in/sign-in/"
        actual_url = driver.current_url

        assert expected_url != actual_url, "URLs should not match"


    def test_menu_items_list(self, setup):
        driver, wait = setup
        page = LoginPage(driver)
        page.click_login()

        page.enter_user_details("vimalcedric26@gmail.com","Cassy@091124")
        page.submit_login()
        page.menu_items()
        page.click_dobby()


    def test_log_out(self, setup):
        driver, wait = setup
        page = LoginPage(driver)
        page.click_login()

        page.enter_user_details("vimalcedric26@gmail.com", "Cassy@091124")
        page.submit_login()

        page.open_dropdown()
        page.log_out_btn()


        assert "https://www.guvi.in/" in driver.current_url




