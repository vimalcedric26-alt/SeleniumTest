from behave import when, then
from selenium.webdriver.common.by import By


@when('User clicks on the menu button')
def step_impl(context):
    context.login_page.click_menu_btn()

@when('User click on the Reset app state')
def step_impl(context):
    context.login_page.click_reset_btn()

@when('User clicks on the logout button')
def step_impl(context):
    context.login_page.click_logout_btn()

@then('Application state should be reset successfully')
def step_impl(context):
    cart_badge = context.driver.find_elements(By.CLASS_NAME,"shopping_cart_badge")
    assert len(cart_badge) == 0