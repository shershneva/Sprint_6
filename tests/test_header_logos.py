from pages.headerpage import *
from pages.mainpage import MainPage
from pages.basepage import BasePage
from conftest import *
import pytest
import allure

class TestClickHeaderLogo:
    @allure.title('Проверка перехода по клику на логотип Самоката в шапке')
    def test_click_on_scooter_logo(self, driver, accept_cookie):
        order_page = MainPage(driver)
        order_page.click_header_order_button()
        order_url = order_page.get_current_url()
        logo_scooter = ScooterLogoPage(driver)
        logo_scooter.click_scooter_logo()
        logo_scooter.wait_for_url_change(order_url)
        new_url = logo_scooter.get_current_url()
        assert new_url != order_url and new_url == Urls.url_main

    @allure.title('Проверка редиректа на страницу Дзена по клику на логотип Яндекса в шапке')
    def test_click_on_yandex_logo(self, driver, accept_cookie):
        logo_yandex = YandexLogoPage(driver)
        current_url = logo_yandex.get_current_url()
        logo_yandex.click_yandex_logo()
        logo_yandex.wait_for_url_change(current_url)
        new_url = logo_yandex.get_current_url()
        assert new_url != current_url and new_url == Urls.url_dzen
