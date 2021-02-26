from selenium.webdriver.common.by import By


def test_add_to_cart_display(browser):
    # Data
    dict = {'de': 'In Warenkorb legen', 'en-gb': 'Add to basket', 'es': 'Añadir al carrito',
            'fr': 'Ajouter au panier', 'it': 'Aggiungi al carrello', 'pt': 'Adicionar ao carrinho',
            'ru': 'Добавить в корзину', 'uk': 'Додати в кошик'}
    add_to_cart = (By.CSS_SELECTOR, '.product_main [type="submit"]')

    # Arrange
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    add_to_cart_text = dict.get(browser.current_url.split("/")[3])

    # Act
    cart = browser.find_element(*add_to_cart).text

    # Assert
    assert cart == add_to_cart_text, f"На кнопке добавления в корзину отображается текст {cart!r}, а должен " \
                                     f"{add_to_cart_text!r}"
