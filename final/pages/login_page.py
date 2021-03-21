import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import LoginPageLocators


class Registration(BasePage):

    @allure.step("Вводим адрес электронной почты для регистрации")
    def enter_registration_email(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_MAIL).send_keys(
            f'{str(time.time()).split(".")[0]}@test.com')

    @allure.step("Вводим пароль для регистрации")
    def enter_registration_password(self, password, confirm_password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD).send_keys(confirm_password)

    @allure.step("Нажимаем кнопку зарегистрироваться")
    def click_register(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()

    @allure.step("Проверяем наличие сообщения об успешной регистрации")
    def check_for_message(self):
        successful_message = self.browser.find_element(*LoginPageLocators.SUCCESSFUL_REGISTRATION).text
        assert successful_message == "Thanks for registering!", \
            f"Сообщение об успешной регистрации должно выглядеть как 'Thanks for registering!', " \
            f"а выглядит как {successful_message!r}"

    @allure.step("Проверяем наличие уведомления о том что пароли не совпадают")
    def different_passwords(self):
        wrong_password = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE)
        ).text
        assert wrong_password == "The two password fields didn't match.", f"Отсутствует либо некорректное уведомление о том что пароли не совпадают"

    @allure.step("Проверяем наличие уведомления о том что введён слишком простой пароль")
    def simple_password(self):
        wrong_password = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE)
        ).text
        assert wrong_password == "This password is too short. It must contain at least 9 characters.", f"Отсутствует либо некорректное " \
                                                                                                       f"уведомление о том что пароли не совпадают"
