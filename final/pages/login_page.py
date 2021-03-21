from selenium.webdriver.common.keys import Keys
import time
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Registration(BasePage):

    @allure.step("Вводим адрес электронной почты для регистрации")
    def enter_registration_email(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_MAIL).send_keys(f'{str(time.time()).split(".")[0]}@test.com')

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
            EC.visibility_of_element_located(LoginPageLocators.PASSWORD_MISMATCH)
        ).text
        print(wrong_password)
        assert wrong_password == "The two password fields didn't match.", f"Отсутствует либо некорректное уведомление о том что пароли не совпадают"
