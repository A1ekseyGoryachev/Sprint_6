from selenium.webdriver.common.by import By


class PageTwoLocators:
    DATE_INPUT_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Когда привезти самокат')]")
    DATE_23_AUGUST = (By.XPATH, "//div[contains(@aria-label,'Choose суббота, 23-е августа 2025 г.')]")
    DATE_30_AUGUST = (By.XPATH, "//div[contains(@aria-label,'Choose суббота, 30-е августа 2025 г.')]")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[contains(text(), '* Срок аренды')]")
    RENTAL_PERIOD_2_DAYS = (By.XPATH, "//div[contains(text(), 'двое суток')]")
    RENTAL_PERIOD_7_DAYS = (By.XPATH, "//div[contains(text(), 'семеро суток')]")
    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, 'grey')
    COMMENT_FOR_COURIER = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]")
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")
    ORDER_CONFIRMATION_WINDOW = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
