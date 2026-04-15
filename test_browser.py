from _test_pom.seleniumpractice import Browser

def test_getbrowserpageinfo():
    url = 'https://www.saucedemo.com/'
    browser = Browser(url)
    print(browser.get_title())
    browser.login_()
    browser.close_browser()