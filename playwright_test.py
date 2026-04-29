import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.guvi.in/courses/?current_tab=paidcourse")
    page.get_by_role("button", name="Login").click()
    page.locator("#emailgroup").click()
    page.get_by_role("textbox", name="Email Address").fill("vimalcedric26@gmail.com")
    page.get_by_role("textbox", name="Email Address").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Cassy@091124")
    page.locator("#login-btn").click()
    page.locator(".⭐️3hk5qd-0 > .lucide").first.click()
    page.locator("#account-boxheader").get_by_text("Sign Out").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
