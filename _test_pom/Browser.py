

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import pytest
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def setup():
     options = Options()
     options.add_argument('--headless')
     options.add_argument('--width=650')
     driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=options)

     yield driver
     driver.quit()