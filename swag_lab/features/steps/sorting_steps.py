from behave import when, then
from features.pages.products import Products


@when('User should be able to click on sort_container button')
def step_impl(context):
    context.product_page = Products(context.driver)
    context.product_page.click_container_icon()

@when('User selects "{sort_option}" from dropdown')
def step_impl(context, sort_option):
    context.product_page.select_sort_option(sort_option)

@then('Products should be sorted by price from low to high')
def step_impl(context):
    actual_prices = (context.product_page.get_product_prices())
    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices