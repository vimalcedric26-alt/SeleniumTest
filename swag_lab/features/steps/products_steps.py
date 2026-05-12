from behave import when, then
from features.pages.products import Products
from selenium.webdriver.common.by import By


@when('User randomly selects four available products')
def step_impl(context):
    context.product_page = Products(context.driver)
    context.selected_products = (context.product_page.random_select_four_products())

@when('User should be able to view the cart icon')
def step_impl(context):
    context.product_page.click_cart_icon()

@when('User clicks on the cart button')
def step_impl(context):
    context.product_page.click_cart_icon()

@then('User clicks on the cart button')
def step_impl(context):
    print(context.driver.current_url)
    assert "cart.html" in context.driver.current_url

@then('User should see login error message')
def step_impl(context):
    error_message = context.driver.find_element(By.XPATH,"//h3[@data-test='error']").text
    assert "Epic sadface" in error_message
    print("Error message displayed successfully")

@then('Selected product names and prices should be displayed successfully')
def step_impl(context):
    assert len(context.selected_products) == 4
    for product in context.selected_products:
        print(f"Verified Product: {product[0]} | Price: {product[1]}")

@then('User should be able to reach dashboard page')
def step_impl(context):
    assert "inventory.html" in context.driver.current_url
    print("Dashboard page reached successfully")