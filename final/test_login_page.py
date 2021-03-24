# -*- coding: utf-8 -*-
import time

import allure
import pytest

from .pages.login_page import Registration

registration_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


class TestLoginPage:
    @allure.title("Позитивный тест регистрации пользователя")
    def test_register_user(self, browser):
        # Arrange
        step = Registration(browser, registration_page_link)
        step.open()

        # Act
        step.enter_registration_email()
        step.enter_registration_password()
        step.click_register()

        # Assert
        step.check_for_message()

    @allure.title("Негативный тест регистрации пользователя с несовпадающими паролями")
    @pytest.mark.personal_tests
    def test_different_passwords_register_user(self, browser):
        # Arrange
        step = Registration(browser, registration_page_link)
        step.open()

        # Act
        step.enter_registration_email()
        step.enter_registration_password(str(time.time()) + '1')
        step.click_register()

        # Assert
        step.different_passwords()

    @allure.title("Негативный тест регистрации пользователя со слишком простым паролем")
    @pytest.mark.personal_tests
    def test_simple_password_register_user(self, browser):
        # Arrange
        step = Registration(browser, registration_page_link)
        step.open()

        # Act
        step.enter_registration_email()
        step.enter_registration_password(123, 123)
        step.click_register()

        # Assert
        step.simple_password()
