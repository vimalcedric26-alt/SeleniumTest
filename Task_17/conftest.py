
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def setup():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://v2.zenclass.in/login")
        yield page
        browser.close()

