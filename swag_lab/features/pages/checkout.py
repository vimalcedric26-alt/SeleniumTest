from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

        self.check_out_input = (By.ID, "checkout")

        self.firstname_input = (By.ID, "first-name")
        self.lastname_input = (By.ID, "last-name")
        self.postalcode_input = (By.ID, "postal-code")

        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")

    def check_out_details(self):
        self.driver.find_element(*self.check_out_input).click()

    def checkout_information(self):
        self.driver.find_element(*self.firstname_input).send_keys("Vimal")
        self.driver.find_element(*self.lastname_input).send_keys("Cedric")
        self.driver.find_element(*self.postalcode_input).send_keys("635001")

        self.driver.find_element(*self.continue_btn).click()

        self.driver.find_element(*self.finish_btn).click()