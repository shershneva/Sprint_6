from selenium.webdriver.common.by import By


class OrderPageLocators:
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')  # кнопка Далее

    #первый блок заказа
    INPUT_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')  # поле ввода имени
    INPUT_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # поле ввода фамилии
    INPUT_ADDRESS = (By.XPATH, '//input[contains(@placeholder,"Адрес")]')  # поле ввода адреса
    INPUT_METRO = (By.CLASS_NAME, 'select-search__input')  # поле ввода станции метро
    INPUT_PHONE = (By.XPATH, '//input[contains(@placeholder,"Телефон")]')  # поле ввода телефона

    #второй блок заказа
    INPUT_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]' ) # поле ввода даты
    RENT_PERIOD = (By.CLASS_NAME, 'Dropdown-control')  # поле Срок аренда
    RENT_PERIOD_DAY = (By.XPATH, '//div[text()="сутки"]')  # минимальный срок аренды (сутки)
    COLOR_BLACK = (By.ID, 'black')  # цвет самоката черный
    INPUT_COMMENT = (By.XPATH, '//input[contains(@placeholder,"Комментарий")]')  # поле ввода комментария

    #подтверждение заказа
    ORDER_BUTTON = (By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]') # кнопка Заказать на форме заказа
    ORDER_WINDOW = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    ORDER_YES_BUTTON = (By.XPATH, '//button[text()="Да"]')  # кнопка подтверждения заказа
    ORDER_SUCCESS = (By.XPATH, '//div[contains(@class,"Order_ModalHeader") and text()="Заказ оформлен"]')  # текст в случае успешного заказа
