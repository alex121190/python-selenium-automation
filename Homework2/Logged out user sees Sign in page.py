from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

# wait for 4 sec
sleep(4)

# click the button
driver.find_element(By.ID, 'nav-orders').click()

# verify
assert 'Sign-In' in driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

driver.quit()

