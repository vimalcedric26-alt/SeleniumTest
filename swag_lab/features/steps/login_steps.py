from behave import given, when
from features.pages.login import LoginPage


@given('User navigates to url')
def step_impl(context):
    print("Opening URL")
    context.driver.get("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.driver)


@when('User enters the username "{username}"')
def step_impl(context, username):

    context.login_page.user_name_details(username)


@when('User enters the password "{password}"')
def step_impl(context, password):

    context.login_page.password_details(password)


@when('I click on login button')
def step_impl(context):

    context.login_page.login_click()


@then('User should be redirected to Swag Labs login page')
def step_impl(context):

    assert context.login_page.get_page_title() == "Swag Labs"