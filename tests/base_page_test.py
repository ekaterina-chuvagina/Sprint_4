import allure
from selenium import webdriver
from page_object.base_page_pages import BasePageScooter
from page_object.order_page_pages import OrderPageScooter


class TestLogoScooter:
    driver = None


    @classmethod
    def setup_class(cls):
        firefox_options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        firefox_options.add_argument('--window-size=1280,800')
        cls.driver = webdriver.Firefox(options=firefox_options)

    @allure.title(
        'Проверка перехода по логотипу "Самокат"')
    @allure.description(
        'На странице заказа нажать на логотип "Самокат" и проверить, что перейдет на главную страницу')
    def test_base_page_transition_logo_scooter(self):
        open_order_page = OrderPageScooter(self.driver)
        open_order_page.order_page()
        transition_logo_scooter = BasePageScooter(self.driver)
        transition_logo_scooter.click_logo_scooter()
        transition_logo_scooter.wait_for_logo_scooter()
        url_logo_scooter = self.driver.current_url
        assert url_logo_scooter == 'https://qa-scooter.praktikum-services.ru/'

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()


class TestLogoYandex:
    driver = None

    @classmethod
    def setup_class(cls):
        firefox_options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        firefox_options.add_argument('--window-size=1280,800')
        cls.driver = webdriver.Firefox(options=firefox_options)

    @allure.title(
        'Проверка перехода по логотипу "Яндекс"')
    @allure.description(
        'На странице заказа нажать на логотип "Яндекс" и проверить, что в новом окне откроется главная страница Яндекса')
    def test_base_page_transition_logo_yandex(self):
        open_order_page = OrderPageScooter(self.driver)
        open_order_page.order_page()
        transition_logo_yandex = BasePageScooter(self.driver)
        transition_logo_yandex.click_logo_yandex()
        transition_logo_yandex.wait_for_new_tab_is_opened()
        self.driver.switch_to.window(self.driver.window_handles[1])
        transition_logo_yandex.wait_until_page_is_loaded()
        assert self.driver.current_url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()


