from selenium import webdriver
from selenium.webdriver.common.by import By

VIEW_CART = (By.CSS_SELECTOR, '.basket-mini .btn-group>a')
EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')
ADD_TO_CART = (By.CSS_SELECTOR, '.product_pod [type="submit"]')
BASKET_PRICE = (By.CSS_SELECTOR, '#basket_totals tr:nth-child(2)>th:nth-child(2)')
QUANTITY_IN_CART = (By.CSS_SELECTOR, '.input-group>input')
UPDATE_CART_QUANTITY = (By.CSS_SELECTOR, '.input-group>span')

link = 'http://selenium1py.pythonanywhere.com/catalogue/'

def test_empty_basket():
    # Data
    empty_basket_message = "Ваша корзина пуста Продолжить покупки"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        # Act
        browser.find_element(*VIEW_CART).click()

        # Assert
        empty = browser.find_element(*EMPTY_BASKET).text
        assert empty_basket_message == empty, f"В пустой корзине есть сообщение {empty!r}, " \
                                              f"а должно быть {empty_basket_message!r}"

    finally:
        browser.quit()


def test_change_the_quantity_in_the_cart():

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        # Act
        browser.find_element(*ADD_TO_CART).click()
        browser.find_element(*VIEW_CART).click()
        old_price = (browser.find_element(*BASKET_PRICE).text).split(" ")[0].replace(',', '.')
        print(old_price)
        quantity_in_cart = browser.find_element(*QUANTITY_IN_CART)
        quantity_in_cart.clear()
        quantity_in_cart.send_keys("2")
        browser.find_element(*UPDATE_CART_QUANTITY).click()
        new_price = (browser.find_element(*BASKET_PRICE).text).split(" ")[0].replace(',', '.')
        print(new_price)

        # # Assert
        assert float(new_price) / float(old_price) == 2, f"Цена за 2 книги должна быть в 2 раза выше чем за 1 книгу, " \
                                                         f"фактически разница составляет " \
                                                         f"{float(new_price) / float(old_price)}"

    finally:
        browser.quit()


