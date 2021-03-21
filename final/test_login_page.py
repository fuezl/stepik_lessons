# -*- coding: utf-8 -*-
from .pages.login_page import Registration
import pytest

registration_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


class TestLoginPage:
    @pytest.mark.personal_tests
    def test_register_user(self, browser):
        # Arrange
        step = Registration(browser, registration_page_link)
        step.open()

        # Act
        step.enter_registration_email()
        step.enter_registration_password()

        # Assert
        step.check_for_message()

    @pytest.mark.personal_tests
    def test_different_passwords_register_user(self, browser):
        # Arrange
        step = Registration(browser, registration_page_link)
        step.open()

        # Act
        step.enter_registration_email()
        step.enter_registration_wrong_password()

        # Assert
        step.different_passwords()
        # time.sleep(5)
