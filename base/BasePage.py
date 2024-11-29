from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as WW

class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WW(driver, 10, poll_frequency=1)

    def open_page(self):
        self.driver.get(self.URL)

    def find(self, *args):
       return self.driver.find_element(*args)





