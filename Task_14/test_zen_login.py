from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from .Zen_portal_login import ZenPortalLogin

def test_login_scenario():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(20)
    zen = ZenPortalLogin(driver)
    zen.navigate_url()
    zen.login()
    zen.open_dropdown()
    title_of_page = zen.logout()
    if title_of_page == 'Classify':
        print("Success")
    else:
        print("failed")

def test_negative_scenario():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(20)
    zen = ZenPortalLogin(driver)
    zen.navigate_url()
    result = zen.login()
    zen.open_dropdown()
    zen.logout()
    if result == True:
        print("TestCase Passed! wrong credentials are not allowed to login")
    else:
        print("TestCase Failed! wrong credentials are allowed to login")