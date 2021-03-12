from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    AUTHORIZATION_MAIL = (By.CSS_SELECTOR, '[name="login-username"]')
    AUTHORIZATION_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    AUTHORIZATION_FORGOT_PASSWORD = (By.CSS_SELECTOR, '.well>p>a')
    AUTHORIZATION_SUBMIT = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTRATION_MAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators:
    REVIEW = (By.ID, 'write_review')
    ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main>.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>.alert-success:nth-child(1) .alertinner')
    PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, '#messages>.alert-success:nth-child(1) strong')
    CART_PRICE = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESSFUL_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages>.alert-success:nth-child(1) .alertinner')

class BasketPageLocators:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket_summary')
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')