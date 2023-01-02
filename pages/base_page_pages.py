import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на кнопку "Заказать"')
    def click_button_order_header(self):
        self.driver.find_element(*BasePageLocators.BUTTON_ORDER_HEADER).click()

    @allure.step('Нажать на логотип "Самокат"')
    def click_logo_scooter(self):
        self.driver.find_element(*BasePageLocators.LOGO_SCOOTER).click()

    def wait_for_logo_scooter(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://qa-scooter.praktikum-services.ru/'))

    @allure.step('Нажать на логотип "Яндекс"')
    def click_logo_yandex(self):
        self.driver.find_element(*BasePageLocators.LOGO_YANDEX).click()

    def wait_for_new_tab_is_opened(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.number_of_windows_to_be(2))

    def wait_until_page_is_loaded(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.url_to_be('https://dzen.ru/?yredirect=true'))
