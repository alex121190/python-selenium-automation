from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BOXES = (By.XPATH, "//div[@class='a-section img-wrapper']")

@given('Open Amazon prime page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/amazonprime')
    sleep(2)

@then('Check if there are {number} boxes')
def boxes(context, number):
    boxes = context.driver.find_elements(*BOXES)
    # print(len(boxes))
    if len(boxes) == number:
        print("Все ок")
    else:
        print("Упс, их не 8")