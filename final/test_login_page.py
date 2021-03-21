# -*- coding: utf-8 -*-
from .pages.login_page import Registration
import pytest
import time

registration_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
password = str(time.time())


class TestLoginPage:
    @pytest.mark.personal_tests
    def test_register_user(self, browser):
        # Arrange
        step = Registration(browser, registration_page_link)
        step.open()

        # Act
        step.enter_registration_email()
        step.enter_registration_password(password, password)
        step.click_register()

        # Assert
        step.check_for_message()

    @pytest.mark.personal_tests
    def test_different_passwords_register_user(self, browser):
        # Arrange
        step = Registration(browser, registration_page_link)
        step.open()

        # Act
        step.enter_registration_email()
        step.enter_registration_password(password, password + '1')
        step.click_register()

        # Assert
        step.different_passwords()

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
