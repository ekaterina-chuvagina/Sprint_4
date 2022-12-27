import allure
from selenium import webdriver
from page_object.base_page_pages import BasePageScooter
from page_object.main_page_pages import MainPageScooter
from page_object.order_page_pages import OrderPageScooter
from utils import get_random_phone_number, get_current_date, get_next_date


class TestOrderButtonMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        firefox_options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        firefox_options.add_argument('--window-size=1280,800')
        cls.driver = webdriver.Firefox(options=firefox_options)

    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" на главной странице: с текущей датой')
    @allure.description(
        'На странице найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_main_page_current_date_user_flow_positive(self):
        click_button_order = MainPageScooter(self.driver)
        click_button_order.main_page()
        click_button_order.scroll_button_order()
        click_button_order.click_button_order()

        new_order = OrderPageScooter(self.driver)
        new_order.filling_form_one(
            name='Олег',
            surname='Олегович',
            address='Рыбников пер., 1',
            station='Чистые пруды',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_one_flow(
            date=get_current_date(),
            comment='Supper')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'

    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" на главной странице: со следующей датой')
    @allure.description(
        'На странице найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_main_page_next_date_user_flow_positive(self):
        click_button_order = MainPageScooter(self.driver)
        click_button_order.main_page()
        click_button_order.scroll_button_order()
        click_button_order.click_button_order()
        new_order = OrderPageScooter(self.driver)
        new_order.filling_form_one(
            name='олег',
            surname='олегович',
            address='рыбников пер., 1',
            station='чистые пруды',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_two_flow(
            date=get_next_date(),
            comment='')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'


    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()


class TestOrderButtonBasePage:
    driver = None

    @classmethod
    def setup_class(cls):
        firefox_options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        firefox_options.add_argument('--window-size=1280,800')
        cls.driver = webdriver.Firefox(options=firefox_options)

    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" в header: со текущей датой')
    @allure.description(
        'В header найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_base_page_current_date_user_flow_positive(self):
        open_main_page = MainPageScooter(self.driver)
        open_main_page.main_page()
        click_button_order = BasePageScooter(self.driver)
        click_button_order.click_button_order_header()
        new_order = OrderPageScooter(self.driver)
        new_order.filling_form_one(
            name='Олег',
            surname='Олегович',
            address='Рыбников пер., 1',
            station='Чистые пруды',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_one_flow(
            date=get_current_date(),
            comment='Supper')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'

    @allure.title(
        'Проверка оформления заказа через кнопку "Заказать" в header: со следующей датой')
    @allure.description(
        'В header найти и нажать кнопку "Заказать", заполнить весь флоу позитивного сценария и проверить, что "Заказ оформлен"')
    def test_order_button_base_page_next_date_user_flow_positive(self):
        open_main_page = MainPageScooter(self.driver)
        open_main_page.main_page()
        click_button_order = BasePageScooter(self.driver)
        click_button_order.click_button_order_header()
        new_order = OrderPageScooter(self.driver)
        new_order.filling_form_one(
            name='олег',
            surname='олегович',
            address='рыбников пер., 1',
            station='чистые пруды',
            number=get_random_phone_number())
        new_order.wait_for_form_two()
        new_order.filling_form_about_rent_two_flow(
            date=get_next_date(),
            comment='')
        new_order.wait_for_form_three()
        new_order.click_confirmation_order()
        new_order_title = new_order.get_new_order_title()
        new_order.wait_for_window_order_is_placed()
        assert new_order_title == 'Заказ оформлен'

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()


