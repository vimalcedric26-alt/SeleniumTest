import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Products:
    def __init__(self, driver):
        self.driver = driver
        self.product_names = (By.CLASS_NAME, "inventory_item_name")
        self.product_prices = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_buttons = (By.XPATH, "//button[contains(text(),'Add to cart')]")
        self.product_prices = (By.CLASS_NAME,"inventory_item_price")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.container_input = (By.XPATH,"//select[@class='product_sort_container']")

    def random_select_four_products(self):
        names = self.driver.find_elements(*self.product_names)
        prices = self.driver.find_elements(*self.product_prices)
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)

        selected_indexes = random.sample(range(len(names)), 4)
        selected_products = []

        for i in selected_indexes:
            product_name = names[i].text
            product_price = prices[i].text
            buttons[i].click()
            print(f"Added Product: {product_name} | Price: {product_price}")
            selected_products.append((product_name, product_price))
            return selected_products

    def validate_item_added_cart(self):
        try:
            items_in_cart = self.driver.find_element(*self.add_items_in_cart_loc).text
            return items_in_cart
        except Exception as e:
            print("no items in cart")
            self.click_add_to_cart_btn()

    def is_cart_icon_visible(self):
        return self.driver.find_element(*self.cart_icon).is_displayed()

    def click_cart_icon(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cart_icon)
        ).click()

    def click_container_icon(self):
        self.driver.find_element(*self.container_input).click()

    def select_sort_option(self,option):
        dropdown = Select(self.driver.find_element(*self.container_input))
        dropdown.select_by_visible_text(option)

    def get_product_prices(self):

        prices = self.driver.find_elements(*self.product_prices)

        price_list = []

        for price in prices:
            value = float(price.text.replace("$", ""))

            price_list.append(value)

        return price_list

