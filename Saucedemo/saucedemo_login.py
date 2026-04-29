from selenium.webdriver.ie.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Saucedemo:
    def __init__(self,url):
        self.count = 0
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

        self.username_loc = (By.ID,"user-name")
        self.password_loc = (By.ID,"password")
        self.login_loc = (By.ID,"login-button")
        self.products_loc = (By.XPATH, '//div[@class="inventory_item_name "]')

        self.menu_loc = (By.XPATH,'//button[@id="react-burger-menu-btn"]')
        self.logout_loc =(By.XPATH,'//a[text()="Logout"]')

    def navigate_url(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except:
            print("Unable to navigate url ")
            return False

    def close(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element(*self.username_loc).send_keys("standard_user")
        self.driver.find_element(*self.password_loc).send_keys("secret_sauce")
        self.driver.find_element(*self.login_loc).click()

    def products_list(self):
        products = self.wait.until(
            EC.visibility_of_all_elements_located(self.products_loc)
        )

        product_names = [item.text for item in products]

        print("Product List:", product_names)
        return product_names

    def list_menu(self):
        self.driver.find_element(*self.menu_loc).click()


    def logout(self):
        # self.driver.find_element(*self.logout_loc).click()
        self.wait.until(EC.visibility_of_element_located(self.logout_loc))
        self.wait.until(EC.element_to_be_clickable(self.logout_loc)).click()

if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    mytest = Saucedemo(url)
    mytest.navigate_url()
    mytest.login()
    mytest.products_list()
    mytest.list_menu()
    mytest.logout()
    mytest.close()
