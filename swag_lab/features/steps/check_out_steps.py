from behave import when, then
from features.pages.checkout import Checkout

@when('User clicks on the checkout button')
def step_impl(context):
    context.checkout = Checkout(context.driver)
    context.checkout.check_out_details()

@when('User enters the checkout details and enters the continue button')
def step_impl(context):
    context.checkout.checkout_information()

# @then('User should receive a confirmation upon completion')
# def step_impl(context):
#     assert "checkout" in context.driver.current_url
#     print("Checkout completed successfully")

@then('User should receive a confirmation upon completion')
def step_impl(context):
    assert "checkout-complete" in context.driver.current_url
    print("Order completed successfully")

