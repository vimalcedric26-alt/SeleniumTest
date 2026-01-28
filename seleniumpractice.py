import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Browser:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def __init__(self,url):
        self.url = url

    def launch_application(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except Exception as e:
            print(f"Error in launching website!!, {e}")
            return False

    def get_title(self):
        if self.launch_application(): # if 2+2 == 4: -> go to if block statement else go to else block statement
            return self.driver.title
        else:
            raise Exception ("Error!!! Page title cannot be found due to browser issue")

    def login_(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        time.sleep(3)
        self.driver.save_screenshot("login.png")


    def close_browser(self):
        self.driver.quit() # quit is used for closing all the instances of browser opened by selenium
