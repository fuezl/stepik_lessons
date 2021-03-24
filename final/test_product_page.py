# -*- coding: utf-8 -*-
import allure
import pytest

from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com"


class TestProductPage:
    @allure.title("Проверка наличия полей для ввода на форме ввода отзыва по товару")
    @pytest.mark.personal_tests
    @pytest.mark.parametrize('product', ["/catalogue/coders-at-work_207/",
                                         "/catalogue/coders-at-work_208/",
                                         "/catalogue/coders-at-work_209/"])
    def test_checking_revocation_fields(self, browser, product):
        # Arrange
        step = ProductPage(browser, f"{link}{product}")
        step.open()

        # Act
        step.enter_review()

        # Assert
        step.checking_revocation_fields()
