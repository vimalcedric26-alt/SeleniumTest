from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from POM.load_userdata import ExcelData

class Dashboard:
    def __init__(self,driver):
        self.driver = driver # object variables
        self.filename = "C:/Users/vimal/Desktop/Notes_Guvi/user_details.xlsx"
        self.sheetname = 'user_data'
        self.admin_loc = (By.XPATH,"//span[text()='Admin']")
        self.add_user_btn = (By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.user_role_drpdwn = (By.XPATH,"(//div[@class='oxd-select-text-input'])[1]")
        self.select_user_role = (By.XPATH,"//div[@class='oxd-select-option']")
        self.emp_name_hints = (By.XPATH,"//input[@placeholder='Type for hints...']")
        self.select_first_emp_name = (By.XPATH,"//div[@class='oxd-autocomplete-option']")
        self.username_field = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.drop_loc = (By.XPATH,"//div[@class='oxd-autocomplete-option']")
        self.password_field = (By.XPATH, "(//input[@type='password'])[1]")
        self.status_field = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
        self.select_enabled_ = (By.XPATH, "//span[text()='Enabled']")
        self.confirm_pwd_field = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[4]")
        self.save_btn = (By.CSS_SELECTOR,'button[type="submit"]')
        self.cancel_btn = (By.XPATH,'//button[text()=" Cancel "]')

    def click_admin_menu(self):
        self.driver.find_element(*self.admin_loc).click()

    def click_add_btn(self):
        self.driver.find_element(*self.add_user_btn).click()

    def fill_user_details(self):
        excel_values = ExcelData(self.filename,self.sheetname)
        workbook, worksheet = excel_values.load_excel_wrkbook()
        user_data = excel_values.get_data_(worksheet=worksheet)
        self.driver.find_element(*self.user_role_drpdwn).click()
        role = self.driver.find_elements(*self.select_user_role)
        for user_role in role:  # ESS
            role = user_role.text
            if role == user_data[2]:
                user_role.click()
                break
            elif role == user_data[2]:
                user_role.click()
                break
            else:
                continue

        self.driver.find_element(*self.emp_name_hints).send_keys(user_data[3])
        self.driver.find_elements(*self.drop_loc)
        element = self.driver.find_elements(*self.select_first_emp_name)
        for first_element in range(len(element)):
            element[first_element].click()
            break
        self.driver.find_element(*self.username_field).send_keys(user_data[5])
        self.driver.find_element(*self.password_field).send_keys(user_data[6])
        self.driver.find_element(*self.status_field).click()
        self.driver.find_element(*self.select_enabled_).click()
        self.driver.find_element(*self.confirm_pwd_field).send_keys(user_data[7])

    def click_save_btn(self):
        self.driver.find_element(*self.save_btn).click()

    def click_cancel_btn(self):
        self.driver.find_element(*self.cancel_btn).click()


# Testcase -> click on admin btn and validate add btn is present
# Testcase -> click on admin btn and validate remove btn is present