
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# element locators
item_by_text = lambda name: (By.XPATH, f"//span[@class='a-truncate-cut' and contains(text(),'{name}')]")

# page actions
class CartPage(BasePage):
    def __init__(self, driver, base_url) -> None:
        BasePage.__init__(self, driver)
        self.base_url = base_url

    def go_to(self) -> None:
        BasePage.go_to(self, f'{self.base_url}/gp/cart/view.html')

    def is_product_on_cart(self, name) -> bool:
        # use the correct hhre
        try:
            self.driver.find_element(*item_by_text(name))
            return True
        except:
            return False

