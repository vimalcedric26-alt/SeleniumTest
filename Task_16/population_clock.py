from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Data: url = 'https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live'

class WorldPopulation(Data):
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)
        self.population_element = None

    def start(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        self.population_element = self.wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='counter-ticker is-size-2-mobile']")))

    def get_world_population(self):
        return self.population_element.text





