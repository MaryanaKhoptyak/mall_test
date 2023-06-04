from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DEFAULT_ELEMENT_WAIT_TIMEOUT_SEC = 20

class PageObject(object):

    def __init__(self, driver:webdriver.Chrome, url):
        self.driver = None
        self.url = ""

    def init(self, driver:webdriver.Chrome, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
        