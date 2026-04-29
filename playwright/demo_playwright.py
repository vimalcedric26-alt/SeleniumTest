from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # driver = webdriver.firefox()
    page = browser.new_page()
    page.goto('https://www.saucedemo.com/')
    page.get_by_placeholder("Username").fill('standard_user')
    page.get_by_placeholder("Password").fill('secret_sauce')
    page.locator('#login-button').click()
    expect(page).to_have_title('Swag Labs')
    print("Successfully logged in")
    items = page.locator('.inventory_item_name').all_inner_texts()
    print(items)
    count = 0
    for each_item in items:
        if each_item == 'Sauce Labs Backpack':
            count +=1
            page.locator(f"(//button[@class='btn btn_primary btn_small btn_inventory '])[{count}]").click()
            break

    expect(page.get_by_text('Remove')).to_contain_text('Remove')
    print("Item Sauce Labs Bike Light has been added to cart")
    page.locator('.shopping_cart_badge').click()
    page.locator('#checkout').click()
    page.get_by_placeholder('First Name').fill('Automation')
    page.get_by_placeholder('Last Name').fill('Testing')
    page.get_by_placeholder('Zip/Postal Code').fill('12344')
    page.locator('#continue').click()
    page.get_by_role('button', name="finish").click()






        #

