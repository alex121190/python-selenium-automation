from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_BUTTON_LOCATOR = (By.XPATH, "//a[@id='nav-cart']")
EMPTY_CART = (By.XPATH, "//div[@id='sc-active-cart']//h1[@class='sc-empty-cart-header']")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)

@then('Click the cart icon')
def click_icon(context):
    click_cart = context.driver.find_element(*CART_BUTTON_LOCATOR)
    click_cart.click()
    sleep(3)

@then('Check that {search_text}')
def check_cart(context, search_text):
    assert 'Your Shopping Cart is empty' in context.driver.find_element(*EMPTY_CART).text

