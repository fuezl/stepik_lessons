from selenium import webdriver
from sys import argv
import time

# link = http://suninjuly.github.io/registration1.html
# link = http://suninjuly.github.io/registration2.html

script_name, link = argv
browser = webdriver.Chrome()

try:
    browser.get(link)

    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("test@test.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    browser.quit()
