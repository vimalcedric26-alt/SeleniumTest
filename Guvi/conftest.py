import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def setup():
    options = Options()
    # options.set_preference("dom.webnotifications.enabled", False)
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-geolocation")

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=options)
    driver.get("https://www.guvi.in/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 15)


    yield driver, wait

    driver.quit()