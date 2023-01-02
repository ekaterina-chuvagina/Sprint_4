from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS = By.XPATH, "//div[contains(@class, 'accordion__item')]//div[contains(@class, 'accordion__heading')]"
    QUESTIONS_SECTION = By.XPATH, "//div[contains(@class, 'Home_FAQ_')]"  # раздел-контейнер "Вопросы о важном"
    CURRENT_ANSWER = By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]"  # текущий ответ
    BUTTON_COOKIE = By.XPATH, "//button[contains(@class, 'App_CookieButton_')]"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[contains(@class, 'Button_Button')]"


