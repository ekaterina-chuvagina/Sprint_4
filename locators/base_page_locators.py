from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_ORDER_HEADER = By.XPATH, "//div[contains(@class, 'Header_Nav_')]//button[contains(@class, 'Button_Button')]"
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'Header_LogoYandex_')]"
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class, 'Header_LogoScooter_')]"
