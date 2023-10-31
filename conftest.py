import pytest
from selenium import webdriver
from staticdata import Urls
from locators.mainpage_locators import CookieLocators

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.url_main)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def accept_cookie(driver):
    driver.find_element(*CookieLocators.COOKIE_AGREE_BUTTON).click()
