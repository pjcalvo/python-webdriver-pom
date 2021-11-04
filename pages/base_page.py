"""
BasePage defines common pages methods
"""


# page actions
class BasePage:
    def __init__(self, driver: object, *args: object) -> None:
        self.driver = driver

    def go_to(self, url: str) -> None:
        self.driver.get(url)

    def get_title(self) -> str:
        return self.driver.title

    def get_url(self) -> str:
        return self.driver.url

