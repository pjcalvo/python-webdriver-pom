
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# element locators
add_to_cart_btn = (By.ID, "add-to-cart-button")

# page actions
class ProductPage(BasePage):
    def __init__(self, driver) -> None:
        BasePage.__init__(self, driver)

    def add_product_to_cart(self) -> None:
        # use the correct hhre
        self.driver.find_element(*add_to_cart_btn).click()
        # I noticed that amazon shows recommendations before adding the product to the cart
        # those recommendations are different for each product
        # so I am adding a sleep here to avoid dealing with each case
        time.sleep(2)
