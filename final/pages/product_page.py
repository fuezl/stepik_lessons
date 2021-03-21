import allure

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    @allure.step("Нажимаем кнопку отзыва в карточке товара")
    def enter_review(self):
        self.browser.find_element(*ProductPageLocators.REVIEW).click()

    @allure.step("Проверяем наличие полей ввода в отзыве")
    def checking_revocation_fields(self):
        assert len(
            self.browser.find_elements(*ProductPageLocators.REVIEW_HEADER)) > 0, "Отсутствует поле ввода заголовка отзыва"
        assert len(
            self.browser.find_elements(*ProductPageLocators.REVIEW_MESSAGE)) > 0, "Отсутствует поле ввода сообщения отзыва"
        assert len(
            self.browser.find_elements(*ProductPageLocators.TITLE_OF_REVIEW)) > 0, "Отсутствует поле ввода названия отзыва"
        assert len(
            self.browser.find_elements(*ProductPageLocators.REVIEW_EMAIL)) > 0, "Отсутствует поле ввода электронной почты для отзыва"