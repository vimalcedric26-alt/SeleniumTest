
from POM.invoking_browser import Browser
from POM.Dashboard import Dashboard
from POM.login import Login

def test_login_scenario():
    launch_browser = Browser()
    firefox_browser = launch_browser.invoke_browser()
    user_login = Login(firefox_browser)
    user_login.navigate_url()
    url_of_page = user_login.login_()
    if url_of_page == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index':
        print("Successfully logged in, TestCase Passed")
    else:
        print("Unable to log in, TestCase Failed")

def test_negative_scenario():
    launch_browser = Browser()
    firefox_browser = launch_browser.invoke_browser()
    user_login = Login(firefox_browser)
    user_login.navigate_url()
    url = user_login.login_()
    result = user_login.check_for_unsuccessfull_login()
    if result == True:
        print("TestCase Passed! wrong credentials are not allowed to login")
    else:
        print("TestCase Failed! wrong credentials are allowed to login")

def test_user_admin_creation():
    launch_browser = Browser()
    firefox_browser = launch_browser.invoke_browser()
    user_login = Login(firefox_browser)
    user_login.navigate_url()
    user_login.login_()
    dashboard_ = Dashboard(firefox_browser)
    dashboard_.click_admin_menu()
    dashboard_.click_add_btn()
    dashboard_.fill_user_details()

def test_cancel_btn_from_add_user():
    launch_browser = Browser()
    firefox_browser = launch_browser.invoke_browser()
    user_login = Login(firefox_browser)
    user_login.navigate_url()
    user_login.login_()
    dashboard_ = Dashboard(firefox_browser)
    dashboard_.click_admin_menu()
    dashboard_.click_add_btn()
    dashboard_.cancel_btn()


    # if url_of_page == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser':
    #     print("Successfully clicked on admin menu, TestCase Passed")
    # else:
    #     print("Unable to click on admin menu, TestCase Failed")
