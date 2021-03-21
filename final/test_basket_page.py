# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.basket_page import BasketPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/'


class TestBasket:
    @pytest.mark.personal_tests
    def test_empty_basket(self, browser):
        # Arrange
        step = BasketPage(browser, link)
        step.open()

        # Act
        step.go_to_the_basket()

        # Assert
        step.checking_the_correctness_of_the_message()

    # def test_change_the_quantity_in_the_cart():
    #
    #     try:
    #         # Arrange
    #         browser = webdriver.Chrome()
    #         browser.implicitly_wait(5)
    #         browser.get(link)
    #
    #         # Act
    #         browser.find_element(*ADD_TO_CART).click()
    #         browser.find_element(*VIEW_CART).click()
    #         old_price = (browser.find_element(*BASKET_PRICE).text).split(" ")[0].replace(',', '.')
    #         print(old_price)
    #         quantity_in_cart = browser.find_element(*QUANTITY_IN_CART)
    #         quantity_in_cart.clear()
    #         quantity_in_cart.send_keys("2")
    #         browser.find_element(*UPDATE_CART_QUANTITY).click()
    #         new_price = (browser.find_element(*BASKET_PRICE).text).split(" ")[0].replace(',', '.')
    #         print(new_price)
    #
    #         # # Assert
    #         assert float(new_price) / float(old_price) == 2, f"Цена за 2 книги должна быть в 2 раза выше чем за 1 книгу, " \
    #                                                          f"фактически разница составляет " \
    #                                                          f"{float(new_price) / float(old_price)}"
    #
    #     finally:
    #         browser.quit()
