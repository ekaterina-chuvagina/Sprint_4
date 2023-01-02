import allure
import pytest
from pages.main_page_pages import MainPageScooter

@pytest.mark.usefixtures("driver")
class TestQuestionsSections:

    sections_test_data = [
        (1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
        (2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
        (3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
        (4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
        (5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
        (6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
        (7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
        (8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
    ]

    @allure.title(
        'Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description(
        'На главной странице найти раздел, нажать на вопросы и проверить, что текст ответов соответствующий')
    @pytest.mark.parametrize("num,text", sections_test_data)
    def test_get_answer(self, driver, num, text):
        question_section = MainPageScooter(driver)
        question_section.main_page()
        question_section.scroll_to_questions_section()
        question_section.wait_for_scroll_to_questions_section()
        question_section.click_question_button(num)
        current_answer = question_section.get_current_answer_text()
        question_section.wait_for_to_get_current_answer()
        assert current_answer == text

