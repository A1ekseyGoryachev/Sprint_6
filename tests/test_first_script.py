import allure


from pages.page_one import PageOne
from data import *
from pages.page_two import PageTwo
from pages.transitions import Transitions
from curl import *


class TestOrderAccordingFirstScript:
    @allure.title("Заполнение форм заказа самоката по первому сценарию")
    def test_order_form_with_first_script(self, driver):
        name = FirstScript.name
        last_name = FirstScript.last_name
        address = FirstScript.address
        phone = FirstScript.phone
        first_script_page_one = PageOne(driver)
        first_script_page_one.press_main_page_upper_order_button()
        first_script_page_one.press_cookies_button()
        first_script_page_one.fill_up_order_form_page_one(name, last_name, address, phone)
        first_script_page_one.press_next_button()
        first_script_page_two = PageTwo(driver)
        comment = FirstCommentForCourier.comment_for_first_script
        first_script_page_two.fill_up_order_form_page_two_with_first_set_of_data(comment)
        first_script_page_two.press_order_button()
        first_script_page_two.press_yes_button()
        order_confirmation = first_script_page_two.get_text_confirmation()
        assert order_confirmation == CHECKUP_STATUS

    @allure.title("Проверка перехода со страницы оформления заказа на главную страницу сайта")
    def test_transition_from_order_page_to_main_page(self, driver):
        name = FirstScript.name
        last_name = FirstScript.last_name
        address = FirstScript.address
        phone = FirstScript.phone
        first_script_page_one = PageOne(driver)
        first_script_page_one.press_main_page_upper_order_button()
        first_script_page_one.press_cookies_button()
        first_script_page_one.fill_up_order_form_page_one(name, last_name, address, phone)
        first_script_page_one.press_next_button()
        first_script_page_two = PageTwo(driver)
        comment = FirstCommentForCourier.comment_for_first_script
        first_script_page_two.fill_up_order_form_page_two_with_first_set_of_data(comment)
        first_script_page_two.press_order_button()
        first_script_page_two.press_yes_button()
        scooter_transition = Transitions(driver)
        scooter_transition.press_confirmation_button()
        scooter_transition.press_scooter_button()
        assert scooter_transition.get_scooter_url() == main_site

    @allure.title("Проверка перехода со страницы оформления заказа на страницу Яндекс.Дзен")
    def test_transition_from_order_page_to_dzen_page(self, driver):
        name = FirstScript.name
        last_name = FirstScript.last_name
        address = FirstScript.address
        phone = FirstScript.phone
        first_script_page_one = PageOne(driver)
        first_script_page_one.press_main_page_upper_order_button()
        first_script_page_one.press_cookies_button()
        first_script_page_one.fill_up_order_form_page_one(name, last_name, address, phone)
        first_script_page_one.press_next_button()
        first_script_page_two = PageTwo(driver)
        comment = FirstCommentForCourier.comment_for_first_script
        first_script_page_two.fill_up_order_form_page_two_with_first_set_of_data(comment)
        first_script_page_two.press_order_button()
        first_script_page_two.press_yes_button()
        dzen_transition = Transitions(driver)
        dzen_transition.press_confirmation_button()
        dzen_transition.press_dzen_button()
        assert dzen_transition.switch_and_get_url(expected_url) == expected_url
