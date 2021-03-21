import allure

from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):

    @allure.step("Переходим в корзину")
    def go_to_the_basket(self):
        self.browser.find_element(*BasketLocators.VIEW_BASKET).click()

    @allure.step("Проверяем правильность сообщения в пустой корзине")
    def checking_the_correctness_of_the_message(self):
        empty_basket_message = self.browser.find_element(*BasketLocators.EMPTY_BASKET).text
        assert empty_basket_message == "Your basket is empty. Continue shopping", f"В пустой корзине должно быть сообщение " \
                                                                                  f"'Your basket is empty. Continue shopping', а отображается {empty_basket_message!r}"
