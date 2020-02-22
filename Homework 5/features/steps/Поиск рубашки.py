from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = (By.ID, "twotabsearchtextbox")
SEARCH_BUTTON_LOCATOR = (By.XPATH, "//div[@id='nav-search']//input[@type='submit']")
FIRST_RESULT = (By.CSS_SELECTOR, '.s-search-results > div[data-index]')
ITEM_LOCATOR = (By.CSS_SELECTOR, 'a')
COLOR_LOCATOR = (By.CSS_SELECTOR, '#variation_color_name ul li')
COLOR_TITLE = (By.XPATH, "//div[@id='variation_color_name']//span[@class='selection']")
ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-button')

@given('Open Amazon page 1')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')
    sleep(2)

@when('Input {search_text} into field')
def search(context, search_text):
    search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search_input.clear()
    search_input.send_keys(search_text)
    sleep(2)

@then('Click search')
def button(context):
    help_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    help_button.click()
    sleep(3)

@then('Choose first result')
def first(context):
    first_result = context.driver.find_elements(*FIRST_RESULT)[0]
    click_result = first_result.find_element(*ITEM_LOCATOR).click()
    sleep(3)

@then('Get all colors')
def color(context):
    context.color_element = context.driver.find_elements(*COLOR_LOCATOR)
    color_title = context.driver.find_element(*COLOR_TITLE)
    for shirt_color in context.color_element:
        shirt_color.click()
        print(color_title.text)

@then('Add {need_color} shirt to the cart')
def needed_color(context, need_color):
    for shirt_color in context.color_element:
        if need_color in shirt_color.get_attribute('title'):
            shirt_color.click()
            sleep(3)
            add_to_cart = context.driver.find_element(*ADD_TO_CART).click()