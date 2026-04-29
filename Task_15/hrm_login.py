from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Task_15.load_exceldata import ExcelData


class Login:

    def __init__(self, driver, filename):
        self.driver = driver
        self.filename = filename
        self.sheetname = "user_data"

        self.username_loc = (By.NAME, "username")
        self.password_loc = (By.NAME, "password")
        self.login_btn_loc = (By.XPATH, "//button[@type='submit']")

    def navigate_url(self):
        self.driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

    def login_hrm(self, user_data, row_number):

        self.navigate_url()
        wait = WebDriverWait(self.driver, 10)

        excel_value = ExcelData(self.filename, self.sheetname)
        workbook, worksheet = excel_value.load_excel_wrkbook()

        try:
            wait.until(
                EC.visibility_of_element_located(self.username_loc)
            ).send_keys(user_data[1])

            wait.until(
                EC.visibility_of_element_located(self.password_loc)
            ).send_keys(user_data[2])

            wait.until(
                EC.element_to_be_clickable(self.login_btn_loc)
            ).click()

            wait.until(EC.url_contains("dashboard"))

            excel_value.update_result(worksheet, row_number, "PASS")
            excel_value.save_workbook(workbook)

            return "PASS"

        except Exception:
            excel_value.update_result(worksheet, row_number, "FAIL")
            excel_value.save_workbook(workbook)

            return "FAIL"