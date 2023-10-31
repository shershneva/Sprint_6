from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from locators.header_locators import HeaderLocators
from staticdata import Urls
import allure

class ScooterLogoPage(BasePage):

    @allure.step('Нажимаем на логотип Самоката в шапке')
    def click_scooter_logo(self):
        self.click_element(HeaderLocators.LOGO_SCOOTER)

class YandexLogoPage(BasePage):

    @allure.step('Нажимаем на логотип Яндекса в шапке')
    def click_yandex_logo(self):
        self.click_element(HeaderLocators.LOGO_YANDEX)
        self.switch_to_new_window()
        self.wait_until_element_visibility(30, HeaderLocators.DZEN_LOGO)


