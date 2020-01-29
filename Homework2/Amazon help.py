from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

# wait for 8 sec
sleep(8)

# click the button
driver.find_element(By.XPATH, "//div[@id='navFooter']//li[@class='nav_last']/a[text()='Help']").click()

search = driver.find_element(By.XPATH, "//input[@name='help_keywords']")
search.clear()
search.send_keys('Cancel Items or Orders')

driver.find_element(By.XPATH, "//span[@id='helpSearchSubmit']//input[@type='submit']").click()

# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']//h1").text

driver.quit()




