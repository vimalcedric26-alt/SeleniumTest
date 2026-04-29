import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def setup():

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )

    yield driver

    driver.quit()