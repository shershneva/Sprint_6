from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from locators.order_locators import OrderPageLocators
import allure

class OrderPage(BasePage):
    @allure.step('Вводим имя')
    def input_name(self, name):
        self.send_keys(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Вводим фамилию')
    def input_surname(self, surname):
        self.send_keys(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step('Вводим адрес')
    def input_address(self, address):
        self.send_keys(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Выбираем станцию метро')
    def choose_metrostation(self):
        self.click_element(OrderPageLocators.INPUT_METRO)
        self.arrowdown_list()
        self.arrowdown_list()
        self.arrowdown_list()
        self.enter_element()

    @allure.step('Вводим телефон')
    def input_phone(self, phone):
        self.send_keys(OrderPageLocators.INPUT_PHONE, phone)

    @allure.step('Нажимаем Далее')
    def press_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем всю первую страницу')
    def fill_order_first_page(self, name, surname, address, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choose_metrostation()
        self.input_phone(phone)
        self.press_next()

    @allure.step('Выбираем дату аренды')
    def choose_date(self):
        self.click_element(OrderPageLocators.INPUT_DATE)
        self.arrowdown_list()
        self.arrowdown_list()
        self.enter_element()

    @allure.step('Выбираем период аренды')
    def choose_rent_period(self):
        self.click_element(OrderPageLocators.RENT_PERIOD)
        self.wait_until_element_visibility(10, OrderPageLocators.RENT_PERIOD_DAY)
        self.click_element(OrderPageLocators.RENT_PERIOD_DAY)

    @allure.step('Выбираем цвет')
    def choose_color(self):
        self.click_element(OrderPageLocators.COLOR_BLACK)

    @allure.step('Вводим комментарий')
    def add_comment(self, comment):
        self.send_keys(OrderPageLocators.INPUT_COMMENT, comment)

    def fill_order_second_page(self, comment):
        self.choose_date()
        self.choose_rent_period()
        self.choose_color()
        self.add_comment(comment)

    def press_order(self):
        self.wait_until_element_visibility(10, OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_until_element_visibility(10, OrderPageLocators.ORDER_WINDOW)
        self.click_element(OrderPageLocators.ORDER_YES_BUTTON)
        self.enter_element()




