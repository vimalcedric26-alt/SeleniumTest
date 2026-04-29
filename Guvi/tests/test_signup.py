from Guvi.pages.signup import SignupPage

class TestSignup:

    def test_signup_form(self, setup):
        driver, wait = setup
        page = SignupPage(driver)
        page.click_signup_button()

        assert "register" in driver.current_url

    def test_positive_signup_btn(self, setup):
        driver, wait = setup
        page = SignupPage(driver)
        page.click_signup_button()

        page.enter_signup_details(
            "Vimal",
            "vimal12@gmail.com",
            "test@091124"
        )
        page.enter_mobile('9738875145')


        assert "register" in driver.current_url
