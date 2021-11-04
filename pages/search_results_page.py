
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

PLACEHOLDER = 'placeholder';

# element locators
link_by_href = lambda href: (By.XPATH, f"//a[contains(@href, '{href}')]")

# page actions
class SearchResultsPage(BasePage):
    def __init__(self, driver) -> None:
        BasePage.__init__(self, driver)

    def select_product_by_href(self, href) -> None:
        self.driver.find_element(*link_by_href(href)).click()
