from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # driver = webdriver.firefox()
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.locator("[name='username']").fill('Admin') # driver.find_element(By.locator_address).send_keys()
    page.locator("[name='password']").fill('admin123')
    page.locator("[type='submit']").click()
    page.get_by_role("link", name="Admin").click()
    page.get_by_role("button",name="Add").click()
    page.get_by_text("Select").first.click()
    page.get_by_role("option",name="Admin").click()
    page.get_by_role("textbox", name="Type for hints...").click()
    page.get_by_role("textbox", name="Type for hints...").fill("Vimal")
    page.get_by_text("Select").first.click()
    page.get_by_role("option", name="Enabled").click()
    page.locator("[name='username']").fill('test123')
    page.locator("[name='password']").fill('test123')
    page.get_by_role("button", name="Save").click()



    # page.close()
    # browser.close()





