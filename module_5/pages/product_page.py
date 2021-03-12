from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def checking_the_correctness_of_messages(self):
        # self.solve_quiz_and_get_code()
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_ADD_TO_BASKET), \
            "Отсутствует сообщение о добавлении товара в корзину"
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        product_added_to_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_CART).text
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert book_name == product_added_to_cart, \
            "Название товара не совпадает с названием товара добавленного в корзину"
        assert book_price == cart_price, "Цена товара в корзине не соответствует цене товара"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message does not disappear"
