from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self.username_loc  = (By.NAME,"user-name")
        self.password_loc = (By.NAME,"password")
        self.login_loc = (By.NAME,'login-button')
        self.item_header_loc = (By.XPATH,'//span[@class="title"]')
        self.driver = driver

    def navigate_url(self,url):
        try:
            self.driver.get(url)
            return True
        except:
            raise Exception("Error navigating to login page ")

    def enter_username_details(self,username):
        self.driver.find_element(*self.username_loc).send_keys(username)

    def enter_password_details(self,password):
        self.driver.find_element(*self.password_loc).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_loc).click()
        try:
            get_item_header = self.driver.find_element(By.XPATH,'//span[@class="title"]').text
            return get_item_header
        except:
            raise Exception("Error to login page ")
