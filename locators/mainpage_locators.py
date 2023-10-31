from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS_ACCORDION = By.XPATH, '//*[@id="accordion__heading-{}"]'  #Блок с вопросами
    ANSWERS_ACCORDION = By.XPATH, '//*[@id="accordion__panel-{}"]'  #Ответы в блоке с вопросами
    HEADER_ORDER_BUTTON = (By.XPATH, '//*[contains(@class,"Header_Nav")]//button[text()="Заказать"]')  # кнопка "Заказать" в шапке
    CENTER_ORDER_BUTTON = (By.XPATH, '//*[contains(@class,"FinishButton")]//button[text()="Заказать"]') # кнопка "Заказать" под блоком "Как это работает"

class CookieLocators:
    COOKIE_INFO_BLOCK = (By.XPATH, '//*[contains(@class,"CookieConsent")]')  # всплывающее окно с вопросом про куки
    COOKIE_AGREE_BUTTON = (By.ID, 'rcc-confirm-button')  # кнопка принятия кук "Да все привыкли"