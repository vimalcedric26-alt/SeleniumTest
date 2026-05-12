from behave import when, then


@when('User should be able to verify the item added in the cart')
def step_impl(context):
    context.login_page.validate_item_added_cart()

@then('User should be able to view the cart icon')
def step_impl(context):
    assert context.login_page.is_cart_icon_visible()

@then('User should be able to click on cart button')
def step_impl(context):
    context.login_page.click_add_to_cart_btn()

@then('Cart page should be displayed successfully')
def step_impl(context):
    assert "cart.html" in context.driver.current_url
    print("Cart page displayed successfully")