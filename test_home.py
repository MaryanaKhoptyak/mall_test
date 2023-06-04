from selenium import webdriver as wd
from pageobjects.home import *

def setup():
    driver = wd.Chrome()
    driver.maximize_window()

    # init all page objects here
    HomeScreen.init(driver)

def test_caoursels():
    HomeScreen.open()

    carousels = HomeScreen.get_carousels()

    for carousel in carousels:
        verify_carousel_items_unique(carousel, 15)


def verify_carousel_items_unique(carousel, min_items):
    # check for minimal size of carousel
    assert min_items <= len(carousel), f"One of Home carousels has less than {min_items} elements"

    # check for distinction, use set trick as list size is not big
    assert len(set(carousel)) == len(carousel), f"One of Home carousels has duplicate items"
    