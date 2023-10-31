from pages.basepage import BasePage
from locators.mainpage_locators import MainPageLocators
from selenium.webdriver.common.by import By
from conftest import *
import allure


class MainPage(BasePage):
    @allure.step('Кликаем на вопросы')
    def click_on_question(self, question):
        self.wait_until_element_visibility(15, question)
        self.find_element(question)
        self.click_element(question)

    @allure.step('Получаем текст ответа на каждый вопрос')
    def get_answer_text(self, answer):
        self.wait_until_element_visibility(15, answer)
        return self.get_element_text(answer)

    @allure.step('Переходим на страницу заказа при клике на кнопку "Заказать" на главной стр.')
    def click_center_order_button(self):
        self.click_element(MainPageLocators.CENTER_ORDER_BUTTON)

    @allure.step('Переходим на страницу заказа при клике на кнопку "Заказать" в шапке')
    def click_header_order_button(self):
        self.click_element(MainPageLocators.HEADER_ORDER_BUTTON)



