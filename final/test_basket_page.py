# -*- coding: utf-8 -*-

import allure
import pytest

from .pages.basket_page import BasketPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/'


class TestBasket:
    @pytest.mark.personal_tests
    @allure.title("Проверка наличия корректного сообщения в пустой корзине")
    def test_empty_basket(self, browser):
        # Arrange
        step = BasketPage(browser, link)
        step.open()

        # Act
        step.go_to_the_basket()

        # Assert
        step.checking_the_correctness_of_the_message()
