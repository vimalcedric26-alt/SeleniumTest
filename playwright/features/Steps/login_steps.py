import time

from behave import given, when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from playwright.features.page_locator.login import Login
from playwright.features.page_locator.products import Products
from playwright.features.login_data.read_excel_data import username,password
from playwright.features.login_data.read_json_data import usernam,pwd


@given('User navigates to url')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.login_page = Login(driver=context.driver)
    context.login_page.navigate_url("https://www.saucedemo.com/")

@when('User enters the username "{username}"')
def step_impl(context,username):
    context.login_page.enter_username_details(username=username)
    # context.driver.find_element(By.NAME,'user-name').send_keys("standard_user")

@when('User enters the password "{password}"')
def step_impl(context,password):
    context.login_page.enter_password_details(password=password)
    # context.driver.find_element(By.NAME,'password').send_keys("secret_sauce")

@when('I click on login button')
def step_impl(context):
    context.login_page.click_login()
    # context.driver.find_element(By.NAME, 'login-button').click()

@when('User is able to pick item "{item}" and click on add to cart button')
def step_impl(context,item):
    context.products = Products(context.driver)
    time.sleep(3)
    context.products.selecting_items(item)

@when('User enters the username from excel-sheet')
def step_impl(context):
    context.login_page.enter_username_details(username=username)

@when('User enters the password from excel-sheet')
def step_impl(context):
    context.login_page.enter_password_details(password=password)

@when('User enters the username from json files')
def step_impl(context):
    context.login_page.enter_username_details(username=usernam)

@when('User enters the password from json files')
def step_impl(context):
    context.login_page.enter_password_details(password=pwd)

@then('I should be able to reach dashboard page')
def step_impl(context):
    landing_page = context.driver.find_element(By.XPATH,'//span[@class="title"]').text
    assert landing_page == 'Products','Unable to login,Testcase failed'
    context.driver.quit()

@then ('User should not be navigated to the login page')
def step_impl(context):
    context.driver.find_element(By.NAME, 'login-button').click()
    error_message = context.driver.find_element(By.XPATH,'//h3[@data-test="error"]').text
    assert error_message == 'Epic sadface: Username and password do not match any user in this service','Able to login, Testcase failed'
    context.driver.quit()

@then('User should be able to verify the item added in the cart')
def step_impl(context):
    context.products.validate_item_added_cart()




