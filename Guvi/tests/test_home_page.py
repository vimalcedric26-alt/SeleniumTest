from Guvi.pages.home_page import GuviPage

class TestGuvi:

    def test_positive_url(self, setup):
        driver, wait = setup
        page = GuviPage(driver)

        assert page.get_current_url() == "https://www.guvi.in/"

    def test_negative_url(self, setup):
        driver, wait = setup
        page = GuviPage(driver)

        assert page.get_current_url() != "https://www.gu.in/"

    def test_positive_title(self, setup):
        driver, wait = setup
        page = GuviPage(driver)

        assert page.get_title() == "HCL GUVI | Learn to code in your native language"

    def test_negative_title(self, setup):
        driver, wait = setup
        page = GuviPage(driver)

        assert page.get_title() != "GUVI | Learn to code in your native language"

    def test_login_button(self, setup):
        driver, wait = setup
        page = GuviPage(driver)

        assert page.is_login_button_visible(wait)

    def test_signup_button(self, setup):
        driver, wait = setup
        page = GuviPage(driver)

        assert page.is_signup_button_visible(wait)

    def test_check_in_signup_button(self, setup):
        driver, wait = setup
        # page = GuviPage(driver)
        driver.get("https://www.guvi.in/register")

        assert "register" in driver.current_url




