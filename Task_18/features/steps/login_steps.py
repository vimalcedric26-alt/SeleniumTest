from behave import when, then, given
from selenium import webdriver
from Task_18.features.pages.login import LoginPage


@given('User navigates to url')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()

    context.login_page = LoginPage(driver=context.driver)
    context.login_page.navigate_url("https://classify.zenclass.in/")


@when('User enters username "{username}"')
def step_impl(context, username):
    context.login_page.enter_username(username)


@when('User enters password "{password}"')
def step_impl(context, password):
    context.login_page.enter_password(password)


@when('Click on Login button')
def step_impl(context):
    context.login_page.click_login()

@when('Click on profile button')
def step_impl(context):
    context.login_page.profile_icon_click()

@then('User should be able to click on logout button')
def step_impl(context):
    context.login_page.log_out()
    context.driver.quit()