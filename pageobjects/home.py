from pageobjects._base import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://mall.cz"
#locators
PATH_BIG_CAROUSEL = "//div[@data-testid='cms-carousel']"
PATH_BIG_CAROUSEL_ITEM = ".//li[@data-testid='cms-carousel-slide']//article[@data-scroll-id]"
PATH_SMALL_CAROUSEL = "//div[@class='category-banner']//div[@class='top-icons']"
PATH_SMALL_CAROUSEL_ITEM = ".//li//a[@class='top-icons__link']"
PATH_FOOTER = "//div[@class='footer__bottom']"

# explicit wait in seconds as whole page is loaded dynamically and
# from code perspective there is no definite way to understand that it is loaded
TIMEOUT_PAGE_LOAD_SEC = 10

class HomeScreenPO(PageObject):

    def init(self, driver):
        super().init(driver, URL)

    # Custom PO methods
    def get_carousels(self):
        result = []

        # before searching for carousels, scroll to page bottom as they are loaded asynchronously
        self.scroll_down()
        # and wait for page to load for explicit time since the number of dynamic elements is unknown
        time.sleep(TIMEOUT_PAGE_LOAD_SEC)
        
        # find all big carousels
        big_carousels = self.driver.find_elements(By.XPATH, PATH_BIG_CAROUSEL)
        
        for carousel in big_carousels:
            big_carousel = []

            # parse carousel items and extract unique ids
            items = carousel.find_elements(By.XPATH, PATH_BIG_CAROUSEL_ITEM)

            for item in items:
                big_carousel.append(item.get_attribute("data-scroll-id"))
            
            result.append(big_carousel)


        # find all small carousels
        small_carousels = self.driver.find_elements(By.XPATH, PATH_SMALL_CAROUSEL)
        
        for carousel in small_carousels:
            small_carousel = []

            # parse carousel items and extract unique ids
            items = carousel.find_elements(By.XPATH, PATH_SMALL_CAROUSEL_ITEM)

            for item in items:
                small_carousel.append(item.get_attribute("href"))
            
            result.append(small_carousel)

        # return format
        # [[id1, id2, id3], ...]
        return result


    def scroll_down(self):
        SCROLL_PAUSE_TIME_SEC = 0.5
        # limit scrolling amount if page glitched or something
        MAX_SCREENS = 30

        for _ in range(MAX_SCREENS):
            self.driver.find_element(By.XPATH, "//body").send_keys(Keys.PAGE_DOWN)
            time.sleep(SCROLL_PAUSE_TIME_SEC)

            try:
                footer = self.driver.find_element(By.XPATH, PATH_FOOTER)
                break
            except:
                pass


HomeScreen = HomeScreenPO(None, "")
