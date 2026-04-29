import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_guvi_navigation(driver):
    driver.get("https://www.guvi.in/")
    wait = WebDriverWait(driver, 10)

    # Click Login
    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    # Enter Email
    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("")

    # Enter Password
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("")

    # Click Login
    wait.until(EC.element_to_be_clickable((By.ID, "login-btn"))).click()

    # Navigation
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='LIVE Classes']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Courses']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Practice']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Resources']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Our Products']"))).click()

    assert "GUVI" in driver.title
