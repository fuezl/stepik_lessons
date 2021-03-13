from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find('login') != -1, "В адресной строке отсутствует 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_MAIL), \
            "Не найдено поле ввода адреса электронной почты при авторизации"
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_PASSWORD), \
            "Не найдено поле ввода пароля при авторизации"
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_FORGOT_PASSWORD), \
            "Не найдена гиперссылка 'Я забыл пароль'"
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_SUBMIT), \
            "Не найдена кнопка 'Войти'"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_MAIL), \
            "Не найдено поле ввода адреса электронной почты при регистрации"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), \
            "Не найдено поле ввода пароля при регистрации"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD), \
            "Не найдено поле повторного ввода пароля при регистрации"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), \
            "Не найдена кнопка 'Зарегистрироваться'"

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REGISTRATION_MAIL)
        mail.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        pass2.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        register.click()
