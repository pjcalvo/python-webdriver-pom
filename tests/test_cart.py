import unittest
import sys
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options 

from pages import HomePage, SearchResultsPage, ProductPage, CartPage
from settings import config

class TestCareeristChallenge(unittest.TestCase):
    
    def setUp(self):
        chrome_options = Options()  

        # change the value in the .env file to run in headed   
        if config["HEADLESS"]:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")  
        
        # initialize drivers and pages
        self.driver = webdriver.Chrome(options=chrome_options)
        self.home_page = HomePage(self.driver, config["BASE_URL"])
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver, config["BASE_URL"])

        # navigate to the homepage 
        self.home_page.go_to()

    def test_add_product(self):
        # set test data
        test_product = {
            "name": 'Hi-Ball Drinking Glass 10.5 oz Concord by the Dozen',
            "href": "Stanton-10-5-Hi-Ball-Tumbler-Glass/dp/B01M1BZCGL"
        }

        # start User flow
        self.driver.save_screenshot("screenshot.png") #taking a screenshot for debuggin purposes
        self.home_page.search_product(test_product["name"])
        self.search_results_page.select_product_by_href(test_product["href"])
        self.product_page.add_product_to_cart()
        self.cart_page.go_to()
        assert self.cart_page.is_product_on_cart(test_product["name"]) == True
        

if __name__ == '__main__':
    unittest.main()