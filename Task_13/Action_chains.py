from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get('https://jqueryui.com/droppable/')
    driver.maximize_window()
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    driver.get("https://jqueryui.com/droppable/")
    wait = WebDriverWait(driver,10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    source = wait.until(EC.visibility_of_element_located((By.ID, "draggable")))
    target = wait.until(EC.visibility_of_element_located((By.ID, "droppable")))

    action = ActionChains(driver)
    action.drag_and_drop(source=source,target=target).perform()

def test_drag_and_drop_negative(driver):
    driver.get("https://jqueryui.com/droppable/")

    wait = WebDriverWait(driver, 10)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

    # Locate target only (No drag action)
    target = wait.until(EC.presence_of_element_located((By.ID, "droppable")))

    # Validate it has NOT changed
    assert target.text != "Dropped!"

