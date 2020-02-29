from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

DEALS_LINK_LOCATOR = (By.XPATH, "//div[@id='nav-xshop']//a[@tabindex='47']")
SEARCH_INPUT_LOCATOR = (By.ID, "twotabsearchtextbox")
SEARCH_BUTTON_LOCATOR = (By.XPATH, "//div[@id='nav-search']//input[@type='submit']")
FIRST_RESULT = (By.CSS_SELECTOR, '.s-search-results > div[data-index]')
ITEM_LOCATOR = (By.CSS_SELECTOR, 'a')
ADD_TO_CART = (By.CSS_SELECTOR, '#add-to-cart-button')

@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')
    sleep(2)

@when('Store original windows')
def store_windows(context):
    context.current_window = context.driver.current_window_handle
    all_windows = context.driver.window_handles

@then('Click the Deals link')
def click_blog(context):
    actions = ActionChains(context.driver)
    find = context.driver.find_element(*DEALS_LINK_LOCATOR)
    actions.key_down(Keys.CONTROL).click(find).key_up(Keys.CONTROL).perform()
    # blog_link = context.driver.find_element(*DEALS_LINK_LOCATOR).click()
    context.all_windows = context.driver.window_handles


@then('Switch to the newly opened window')
def new_window(context):
    context.driver.switch_to.window(context.all_windows[1])
    sleep(2)

@then('Look up for {search_text}')
def look_for_shirts(context, search_text):
    search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search_input.clear()
    search_input.send_keys(search_text)

@then('Click search')
def button(context):
    help_button = context.driver.find_element(*SEARCH_BUTTON_LOCATOR)
    help_button.click()
    sleep(3)

@when('Open first item')
def first(context):
    first_result = context.driver.find_elements(*FIRST_RESULT)[0]
    click_result = first_result.find_element(*ITEM_LOCATOR).click()
    sleep(3)

@then('Add it to the cart')
def add_to_cart(context):
    add_to_cart = context.driver.find_element(*ADD_TO_CART)
    add_to_cart.click()

@then('User can switch back to original')
def switch_window(context):
    context.driver.switch_to.window(context.current_window)


@then('Refresh original window')
def refresh(context):
    context.driver.refresh()