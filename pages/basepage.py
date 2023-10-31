from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url='https://qa-scooter.praktikum-services.ru/'):
        return self.driver.get(url)

    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != main_window:
                self.driver.switch_to.window(window_handle)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def wait_until_element_visibility(self, time, locator):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_for_url_change(self, current_url):
        WebDriverWait(self.driver, 20).until(EC.url_changes(current_url))

    def enter_element(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def arrowdown_list(self):
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text




