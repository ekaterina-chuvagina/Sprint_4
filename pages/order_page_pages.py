import time

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators


class OrderPageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу https://qa-scooter.praktikum-services.ru/order')
    def order_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')

    def wait_for_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be('https://qa-scooter.praktikum-services.ru/order'))


    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.FIELD_NAME).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.FIELD_SURNAME).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.FIELD_ADDRESS).send_keys(address)

    def set_subway_station(self, station):
        self.driver.find_element(*OrderPageLocators.FIELD_SUBWAY_STATION).send_keys(station)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.SCROLLABLE_FIELD_SUBWAY_STATION))
        self.click_scrollable_subway_station()

    def click_scrollable_subway_station(self):
        self.driver.find_element(*OrderPageLocators.SCROLLABLE_FIELD_SUBWAY_STATION).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element(OrderPageLocators.SCROLLABLE_FIELD_SUBWAY_STATION))

    def set_phone_number(self, number):
        self.driver.find_element(*OrderPageLocators.FIELD_PHONE).send_keys(number)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.FIELD_PHONE)) #?

    def click_button_forward(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(OrderPageLocators.BUTTON_FORWARD))
        self.driver.find_element(*OrderPageLocators.BUTTON_FORWARD).click()

    @allure.step('Заполнить поля в форме "Для кого самокат?"')
    def filling_form_one(self, name, surname, address, station, number):  #заполнение формы Для кого самокат?
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_subway_station(station)
        self.set_phone_number(number)
        self.click_button_forward()

    def wait_for_form_two(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.FORM_TWO))

    def set_date(self, date):
        self.driver.find_element(*OrderPageLocators.FIELD_CALENDAR).send_keys(date)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.CALENDAR)) # Ждем пока появится календарь
        self.driver.find_element(*OrderPageLocators.DATE_PICKER_DAY_SELECTED).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element(OrderPageLocators.CALENDAR))  # Ждем пока пропадет календарь

    def select_rental_period(self, period_locator):
        self.driver.find_element(*OrderPageLocators.FIELD_RENTAL_PERIOD).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.MENU_RENTAL_PERIOD)) # Ждем пока появится список
        self.driver.find_element(*period_locator).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(OrderPageLocators.MENU_RENTAL_PERIOD)) # Ждем пока пропадет список

    def click_checkbox_black(self):
        self.driver.find_element(*OrderPageLocators.CHECKBOX_BLACK).click()

    def click_checkbox_grey(self):
        self.driver.find_element(*OrderPageLocators.CHECKBOX_GREY).click()

    def set_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.FIELD_COMMENT).send_keys(comment)

    def click_button_order(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(OrderPageLocators.BUTTON_ORDER))
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()

    @allure.step('Заполнить поля в форме "Про аренду"')
    def filling_form_about_rent_one_flow(self, date, comment):  #заполнение формы Про аренду 1
        self.set_date(date)
        self.select_rental_period(OrderPageLocators.RENTAL_PERIOD_DAY)
        self.click_checkbox_grey()
        self.set_comment(comment)
        self.click_button_order()

    @allure.step('Заполнить поля в форме "Про аренду"')
    def filling_form_about_rent_two_flow(self, date, comment): #заполнение формы Про аренду 2
        self.set_date(date)
        self.select_rental_period(OrderPageLocators.RENTAL_PERIOD_SEVEN_DAYS)
        self.click_checkbox_black()
        self.set_comment(comment)
        self.click_button_order()

    def wait_for_form_three(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.FORM_THREE))

    @allure.step('Нажать на кнопку "Да"')
    def click_confirmation_order(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_CONFIRMATION_ORDER).click()

    def wait_for_window_order_is_placed(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.WINDOW_ORDER_IS_PLACED))

    @allure.step('Получить окно с текстом "Заказ оформлен"')
    def get_new_order_title(self):
        new_order_text = self.driver.find_element(*OrderPageLocators.WINDOW_ORDER_IS_PLACED).text
        result = new_order_text.split('\n')
        return result[0]

    def click_button_view_status(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_VIEW_STATUS).click()


