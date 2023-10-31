import pytest
import allure
from staticdata import FAQ
from staticdata import Urls
from pages.basepage import BasePage
from pages.mainpage import MainPage
from locators.mainpage_locators import MainPageLocators
from conftest import *


class TestQuestionAnswers:

    @pytest.mark.parametrize('q_num', range(8))
    @allure.title('Проверка работы раскрывающихся вопросов в блоке Вопросы о важном')
    @allure.description('На странице находим вопрос, нажимаем на него, открывается ответ, сверяем с нужным ответом')
    def test_answer_to_questions(self, driver, accept_cookie, q_num):
        main_page = MainPage(driver)
        q_part1 = MainPageLocators.QUESTIONS_ACCORDION[0]
        q_part2 = MainPageLocators.QUESTIONS_ACCORDION[1].format(q_num)

        main_page.click_on_question((q_part1, q_part2))

        a_part1 = MainPageLocators.ANSWERS_ACCORDION[0]
        a_part2 = MainPageLocators.ANSWERS_ACCORDION[1].format(q_num)
        answer_text = main_page.get_answer_text((a_part1, a_part2))

        expected_text = FAQ.answers[q_num]

        assert answer_text == expected_text

class TestOrderButtons:

    @allure.title('Проверка работы кнопки Заказать в центре страницы')
    def test_click_on_center_button(self, driver, accept_cookie):
        main_page = MainPage(driver)
        main_page.click_center_order_button()
        current_url = main_page.get_current_url()

        assert current_url == Urls.url_order

    @allure.title('Проверка работы кнопки Заказать в шапке')
    def test_click_on_header_button(self, driver, accept_cookie):
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        current_url = main_page.get_current_url()

        assert current_url == Urls.url_order

