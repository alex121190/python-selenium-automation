from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT_LOCATOR = (By.ID, "twotabsearchtextbox")
SEARCH_BUTTON_LOCATOR = (By.XPATH, "//div[@id='nav-search']//input[@type='submit']")
# BOOKS_LOCATOR = (By.CSS_SELECTOR, ".s-result-item")
BOOKS_LOCATOR = (By.XPATH, "//a[@class='a-link-normal']//div[@class='a-section aok-relative s-image-fixed-height']")
# LAST_BOOK_LOCATOR = (By.XPATH, "//a[@class='a-link-normal']//div[@class='a-section aok-relative s-image-fixed-height']")
# LAST_BOOK_PRICE_TAG = ()

@given('Open main Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)

@when('In the search field write {search_text}')
def search(context, search_text):
    search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search_input.clear()
    search_input.send_keys(search_text)
    sleep(2)

@then('Click search button')
def button(context):
    help_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    help_button.click()
    sleep(3)

@then('Count how many books would be shown in result list')
def count(context):
    books = context.driver.find_elements(*BOOKS_LOCATOR)
    print(len(books))

# @when('Find the last book')
# def last_book(context):
#     last_book = context.driver.find_element(*LAST_BOOK_LOCATOR)
#
# @then('Check if the price more that 10$ - add it to cart')
# def price_tag(context):
#     price_tag = context.driver.find_element(*LAST_BOOK_PRICE_TAG)
#
