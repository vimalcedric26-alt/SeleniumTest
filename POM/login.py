
import time
from fileinput import filename

from selenium.webdriver.common.by import By
from POM.load_userdata import ExcelData


class Login:
    def __init__(self,driver):
        self.driver = driver
        self.filename = "C:/Users/vimal/Desktop/Notes_Guvi/user_details.xlsx"
        self.sheetname = 'user_data'
        self.username_loc = By.NAME,'username' # By.Name,'username' ->(name,username)
        self.password_loc = (By.NAME,'password')
        self.login_btn_loc = (By.TAG_NAME,'button')
        self.forgot_pwd_loc = (By.XPATH,"//p[contains(@class,'orangehrm-login-forgot-header')]")
        self.invalid_cred_loc = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def navigate_url(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login_(self):
        excel_values = ExcelData(self.filename,self.sheetname)
        workbook, worksheet = excel_values.load_excel_wrkbook()
        user_data = excel_values.get_data_(worksheet=worksheet)
        self.driver.find_element(*self.username_loc ).send_keys(user_data[0]) # find_element((By.Name,'username'))
        self.driver.find_element(*self.password_loc).send_keys(user_data[1]) # find_element(By.NAME,'password')
        self.driver.find_element(*self.login_btn_loc).click()
        return self.driver.current_url

    def check_for_unsuccessfull_login(self):
        time.sleep(5)
        if self.driver.find_element(*self.invalid_cred_loc).is_displayed():
            return True
        else:
            return False

    def forgot_pwd(self):
        self.driver.find_element(*self.forgot_pwd_loc).click()
