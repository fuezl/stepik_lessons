# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketLocators:
    VIEW_BASKET = (By.CSS_SELECTOR, '.basket-mini .btn-group>a')
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.product_pod [type="submit"]')
    BASKET_PRICE = (By.CSS_SELECTOR, '#basket_totals tr:nth-child(2)>th:nth-child(2)')
    QUANTITY_IN_BASKET = (By.CSS_SELECTOR, '.input-group>input')
    UPDATE_BASKET_QUANTITY = (By.CSS_SELECTOR, '.input-group>span')

class LoginPageLocators:
    AUTHORIZATION_MAIL = (By.CSS_SELECTOR, '[name="login-username"]')
    AUTHORIZATION_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    AUTHORIZATION_FORGOT_PASSWORD = (By.CSS_SELECTOR, '.well>p>a')
    AUTHORIZATION_SUBMIT = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTRATION_MAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')
    SUCCESSFUL_REGISTRATION = (By.CSS_SELECTOR, ".alertinner")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.form-group.has-error .error-block')

class ProductPageLocators:
    REVIEW = (By.CSS_SELECTOR, '#write_review')
    REVIEW_HEADER = (By.CSS_SELECTOR, '#add_review_form [name="title"]')
    REVIEW_MESSAGE = (By.CSS_SELECTOR, '#add_review_form #id_body')
    TITLE_OF_REVIEW = (By.CSS_SELECTOR, '#add_review_form #id_name')
    REVIEW_EMAIL = (By.CSS_SELECTOR, '#add_review_form #id_email')
