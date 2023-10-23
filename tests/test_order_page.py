import allure
import pytest
from conftest import *
from locators.order_locators import OrderPageLocators
from pages.orderpage import OrderPage
from pages.basepage import BasePage
from staticdata import Order
from staticdata import Urls

class TestOrderProcess:
    @allure.title('Проверка процесса заказа самоката')
    @allure.description('По шагам заполняем форму заказа и нажимаем "Заказать"')
    @pytest.mark.parametrize('user', (Order.order_1, Order.order_2))
    def test_order_process(self, driver, accept_cookie, user):
        order = OrderPage(driver)
        order.go_to_site(Urls.url_order)

        order.fill_order_first_page(user[0], user[1], user[2], user[3])
        order.fill_order_second_page(user[4])

        order.press_order()
        order.wait_until_element_visibility(10, OrderPageLocators.ORDER_SUCCESS)
        order_ok = order.get_element_text(OrderPageLocators.ORDER_SUCCESS)

        assert Order.order_success in order_ok