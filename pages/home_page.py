
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# element locators
search_input = (By.ID, "twotabsearchtextbox")
search_icon = (By.ID, "nav-search-submit-button")
cart_icon = (By.ID, "nav-cart-count-container")

# page actions
class HomePage(BasePage):
    def __init__(self, driver, base_url:str) -> None:
        BasePage.__init__(self, driver)
        self.base_url = base_url

    def go_to(self) -> None:
        BasePage.go_to(self, f'{self.base_url}/')

    def search_and_select_product(self, product_name) -> None:
        self.search_product(self, product_name)
        # self.

    def search_product(self, product_name) -> None:
        self.driver.find_element(*search_input).send_keys(product_name)
        self.driver.find_element(*search_icon).click()

    def click_cart_icon(self) -> None:
        self.driver.find_element(*cart_icon).click()
        


