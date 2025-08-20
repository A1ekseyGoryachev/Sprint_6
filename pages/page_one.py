import allure

from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from locators.page_one_locators import PageOneLocators


class PageOne(MainPage):

    @allure.step("Нажать на кнопку заказа в верхнем правом углу главной страницы")
    def press_main_page_upper_order_button(self):
        element = MainPageLocators.ORDER_BUTTON_UP
        self.click_on_element(element)

    @allure.step("Нажать на кнопку заказа в нижней части главной страницы"
                 " после раздела 'Как это работает'")
    def press_main_page_lower_order_button(self):
        element = MainPageLocators.ORDER_BUTTON_DOWN
        self.scroll_to_element(element)
        self.click_on_element(element)

    @allure.step("Нажать на кнопку согласия на использование файлов cookie")
    def press_cookies_button(self):
        element = PageOneLocators.COOKIES_BUTTON
        self.click_on_element(element)

    @allure.step("Заполнить форму заказа на первой странице"
                 " оформления заказа")
    def fill_up_order_form_page_one(self, name, last_name, address, phone):
        self.send_keys_to_input(PageOneLocators.NAME_INPUT, name)
        self.send_keys_to_input(PageOneLocators.LAST_NAME_INPUT, last_name)
        self.send_keys_to_input(PageOneLocators.ADDRESS_INPUT, address)
        self.click_on_element(PageOneLocators.STATION_INPUT)
        self.click_on_element(PageOneLocators.STATION_SELECTION)
        self.send_keys_to_input(PageOneLocators.PHONE_INPUT, phone)

    @allure.step("Нажать на кнопку 'Далее' на первой странице оформления заказа")
    def press_next_button(self):
        element = PageOneLocators.NEXT_BUTTON
        self.click_on_element(element)
