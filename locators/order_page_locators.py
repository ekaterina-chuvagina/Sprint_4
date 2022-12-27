from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIELD_NAME = By.XPATH, "//input[contains(@placeholder, '* Имя')]"
    FIELD_SURNAME = By.XPATH, "//input[contains(@placeholder, '* Фамилия')]"
    FIELD_ADDRESS = By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]"
    FIELD_PHONE = By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]"
    FIELD_SUBWAY_STATION = By.XPATH, "//input[@class='select-search__input']"
    SCROLLABLE_FIELD_SUBWAY_STATION = By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li"
    BUTTON_FORWARD = By.XPATH, "//div[contains(@class, 'Order_NextButton')]/button[contains(@class, 'Button_Button_')]"
    FORM_TWO = By.XPATH, "//div[contains(text(), 'Про аренду')]"
    FIELD_CALENDAR = By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]"
    CALENDAR = By.XPATH, "//div[@class= 'react-datepicker']"
    FIELD_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-root']"  # поле
    MENU_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-menu']"
    RENTAL_PERIOD_DAY = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='сутки')]"  # сутки
    RENTAL_PERIOD_TWO_DAYS = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='двое суток')]"
    RENTAL_PERIOD_THREE_DAYS = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='трое суток')]"
    RENTAL_PERIOD_FOUR_DAYS = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='четверо суток')]"
    RENTAL_PERIOD_FIVE_DAYS = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='пятеро суток')]"
    RENTAL_PERIOD_SIX_DAYS = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='шестеро суток')]"
    RENTAL_PERIOD_SEVEN_DAYS = By.XPATH, "//div[contains(@class, 'Dropdown-option') and (text()='семеро суток')]"
    CHECKBOX_BLACK = By.XPATH, "//div[starts-with(@class, 'Order_Checkboxes')]/*/input[@id='black']"
    CHECKBOX_GREY = By.XPATH, "//div[starts-with(@class, 'Order_Checkboxes')]/*/input[@id='grey']"
    FIELD_COMMENT = By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[contains(@class, 'Button_Button') and (text()='Заказать')]"
    FORM_THREE = By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]"
    BUTTON_CONFIRMATION_ORDER = By.XPATH, "//button[contains(text(), 'Да')]"
    WINDOW_ORDER_IS_PLACED = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"
    BUTTON_VIEW_STATUS = By.XPATH, "//button[contains(text(), 'Посмотреть статус')]"
    DATE_PICKER_DAY_SELECTED = By.XPATH, "//div[contains(@class, 'react-datepicker__week')]/div[contains(@class, 'react-datepicker__day--selected')]"
