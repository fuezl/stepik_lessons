# -*- coding: utf-8 -*-

import allure
import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import Registration

link = 'http://selenium1py.pythonanywhere.com/catalogue/'
registration_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


class TestBasket:
    @pytest.mark.personal_tests
    @allure.title("Проверка наличия корректного сообщения в пустой корзине для гостя")
    def test_empty_basket_guest(self, browser):
        # Arrange
        step = BasketPage(browser, link)
        step.open()

        # Act
        step.go_to_the_basket()

        # Assert
        step.checking_the_correctness_of_the_message()

    @pytest.mark.personal_tests
    @allure.title("Проверка наличия корректного сообщения в пустой корзине для зарегистрированного пользователя")
    def test_empty_basket_user(self, browser):
        # Arrange
        reg = Registration(browser, registration_page_link)
        reg.open()
        reg.enter_registration_email()
        reg.enter_registration_password()
        reg.click_register()
        step = BasketPage(browser, browser.current_url)
        step.open()

        # Act
        step.go_to_the_basket()

        # Assert
        step.checking_the_correctness_of_the_message()
