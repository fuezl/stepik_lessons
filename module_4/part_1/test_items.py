from selenium.webdriver.common.by import By

product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart_display(browser):
    # Data
    lang = {'de': 'In Warenkorb legen',
            'en-gb': 'Add to basket',
            'es': 'Añadir al carrito',
            'fr': 'Ajouter au panier',
            'it': 'Aggiungi al carrello',
            'pt': 'Adicionar ao carrinho',
            'ru': 'Добавить в корзину',
            'uk': 'Додати в кошик'
            }
    add_to_cart_locator = (By.CSS_SELECTOR, '.product_main [type="submit"]')

    # Arrange
    browser.get(product_link)
    expected_btn_text = lang.get(browser.user_language)

    # Act
    cart_text = browser.find_element(*add_to_cart_locator).text

    # Assert
    assert cart_text == expected_btn_text, f"На кнопке добавления в корзину отображается текст {cart_text !r}, " \
                                           f"а должен {expected_btn_text!r}"
