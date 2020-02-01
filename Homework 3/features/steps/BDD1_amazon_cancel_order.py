from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

HELP_BUTTON_LOCATOR = (By.XPATH, "//div[@id='navFooter']//li[@class='nav_last']/a[text()='Help']")
SEARCH_INPUT_LOCATOR = (By.XPATH, "//input[@name='help_keywords']")
SUBMIT_BUTTON_LOCATOR = (By.XPATH, "//span[@id='helpSearchSubmit']//input[@type='submit']")
ASSERT_LOCATOR = (By.XPATH, "//div[@class='help-content']//h1")

@given('Open Amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(7)


@then('Click the help button')
def click_button(context):
    help_button = context.driver.find_element(*HELP_BUTTON_LOCATOR)
    help_button.click()
    sleep(3)

@when('Search input fill {search_text}')
def search_input_fill(context, search_text):
    search_input = context.driver.find_element(*SEARCH_INPUT_LOCATOR)
    search_input.clear()
    search_input.send_keys(search_text)
    sleep(2)

@then('Click submit button')
def click_submit(context):
    submit = context.driver.find_element(*SUBMIT_BUTTON_LOCATOR)
    submit.click()

@then('Assert {search_text}')
def check_cancel(context, search_text):
    assert 'Cancel Items or Orders' in context.driver.find_element(*ASSERT_LOCATOR).text


