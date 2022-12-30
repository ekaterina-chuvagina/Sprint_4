import allure
import pytest
from pages.base_page_pages import BasePageScooter
from pages.order_page_pages import OrderPageScooter

@pytest.mark.usefixtures("driver")
class TestLogoScooter:
    @allure.title(
        'Проверка перехода по логотипу "Самокат"')
    @allure.description(
        'На странице заказа нажать на логотип "Самокат" и проверить, что перейдет на главную страницу')
    def test_base_page_transition_logo_scooter(self, driver):
        open_order_page = OrderPageScooter(driver)
        open_order_page.order_page()
        transition_logo_scooter = BasePageScooter(driver)
        transition_logo_scooter.click_logo_scooter()
        transition_logo_scooter.wait_for_logo_scooter()
        url_logo_scooter = driver.current_url
        assert url_logo_scooter == 'https://qa-scooter.praktikum-services.ru/'


@pytest.mark.usefixtures("driver")
class TestLogoYandex:
    @allure.title(
        'Проверка перехода по логотипу "Яндекс"')
    @allure.description(
        'На странице заказа нажать на логотип "Яндекс" и проверить, что в новом окне откроется главная страница Яндекса')
    def test_base_page_transition_logo_yandex(self, driver):
        open_order_page = OrderPageScooter(driver)
        open_order_page.order_page()
        transition_logo_yandex = BasePageScooter(driver)
        transition_logo_yandex.click_logo_yandex()
        transition_logo_yandex.wait_for_new_tab_is_opened()
        driver.switch_to.window(driver.window_handles[1])
        transition_logo_yandex.wait_until_page_is_loaded()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'



