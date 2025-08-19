import allure


from pages.page_one import PageOne
from data import SecondScript
from data import SecondCommentForCourier
from pages.page_two import PageTwo
from pages.transitions import Transitions
from curl import *

class TestOrderWithSecondScript:
    @allure.title("Заполнение формы заказа со вторым набором данных")
    def test_order_form_with_second_script(self, driver):
        name = SecondScript.name
        last_name = SecondScript.last_name
        address = SecondScript.address
        phone = SecondScript.phone
        second_script_page_one = PageOne(driver)
        second_script_page_one.press_main_page_lower_order_button()
        second_script_page_one.press_cookies_button()
        second_script_page_one.fill_up_order_form_page_one(name, last_name, address, phone)
        second_script_page_one.press_next_button()
        second_script_page_two = PageTwo(driver)
        comment = SecondCommentForCourier.comment_for_second_script
        second_script_page_two.fill_up_order_form_page_two_with_second_set_of_data(comment)
        second_script_page_two.press_order_button()
        second_script_page_two.press_yes_button()
        order_confirmation = second_script_page_two.get_text_confirmation()
        assert order_confirmation == "Посмотреть статус"

    @allure.title("Проверка перехода со страницы оформления заказа на главную страницу сайта")
    def test_transition_from_order_page_to_main_page(self, driver):
        scooter_confirmation = TestOrderWithSecondScript()
        scooter_confirmation.test_order_form_with_second_script(driver)
        scooter_transition = Transitions(driver)
        scooter_transition.press_confirmation_button()
        scooter_transition.press_scooter_button()
        assert scooter_transition.get_scooter_url() == main_site

    @allure.title("Проверка перехода со страницы оформления заказа на страницу Яндекс.Дзен")
    def test_transition_from_order_page_to_dzen_page(self, driver):
        scooter_confirmation = TestOrderWithSecondScript()
        scooter_confirmation.test_order_form_with_second_script(driver)
        dzen_transition = Transitions(driver)
        dzen_transition.press_confirmation_button()
        dzen_transition.press_dzen_button()
        assert dzen_transition.switch_and_get_url(expected_url) == expected_url
