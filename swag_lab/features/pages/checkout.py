
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Checkout:
    def __init__(self,driver):
        self.driver = driver
        # self.check_out_input = (By.XPATH,"//button[@id='checkout']")
        self.firstname_input = (By.NAME,"firstName")
        self.lastname_input = (By.NAME, "lastName")
        self.code_input = (By.NAME, "postalCode")
        self.continue_input = (By.NAME, "continue")
        self.finish_input = (By.NAME,"finish")
        self.check_out_input = (By.ID, "checkout")

    def check_out_details(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.check_out_input)
        ).click()

    def checkout_information(self):
        self.driver.find_element(*self.firstname_input).send_keys("vimal")
        self.driver.find_element(*self.lastname_input).send_keys("cedric")
        self.driver.find_element(*self.code_input).send_keys("560047")

        self.driver.find_element(*self.continue_input).click()
        self.driver.find_element(*self.finish_input).click()

