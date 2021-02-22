import time
from selenium import webdriver
from selenium.webdriver.common.by import By

registration_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

enter_email = '.register_form [type="email"]'
enter_password = '.register_form [name="registration-password1"]'
repeat_password = '.register_form [name="registration-password2"]'
register = '.register_form [name="registration_submit"]'
successful_registration = ".alertinner"
log_out = "#logout_link"
email = f'{str(time.time()).split(".")[0]}@test.com'
password = str(time.time())


def test_register_user():
    # Data
    successful_registration_message = "Спасибо за регистрацию!"
    log_out_of_account = "Выход"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(registration_page_link)

        # Act
        browser.find_element(By.CSS_SELECTOR, enter_email).send_keys(email)
        browser.find_element(By.CSS_SELECTOR, enter_password).send_keys(password)
        browser.find_element(By.CSS_SELECTOR, repeat_password).send_keys(password)
        browser.find_element(By.CSS_SELECTOR, register).click()

        # # Assert
        successful_message = browser.find_element(By.CSS_SELECTOR, successful_registration).text
        assert successful_registration_message == successful_message, \
            f"Сообщение об успешной регистрации должно выглядеть как '{successful_registration_message}', " \
            f"а выглядит как '{successful_message}'"
        log_out_test = browser.find_element(By.CSS_SELECTOR, log_out).text
        assert log_out_test == log_out_of_account, \
            f"На кнопке выхода из аккаунта должен быть текст '{log_out_of_account}', " \
            f"а отображается '{log_out_test}'"

    finally:
        browser.quit()


test_register_user()
