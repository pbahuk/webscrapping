from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--kiosk")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.pluralsight.com/')

# Get Element By Name
element = driver.find_element_by_name("q")
time.sleep(1)
element.clear()
element.send_keys("Prabhat Bahukhandi")
element.send_keys(Keys.RETURN)

# Get Element By Link text
element = driver.find_element_by_name("q")
time.sleep(1)
element.clear()
element.send_keys('Prateerth Padman')
element.send_keys(Keys.RETURN)
# element_link = driver.find_element_by_link_text("Building Image Classification")
# element_link = driver.find_element_by_partial_link_text("Building Image Classification")
time.sleep(1)
# element_link.click()


#Get Element by Xpath
element = driver.find_element_by_xpath("//input[@name='q']")
time.sleep(1)
element.clear()
element.send_keys('Tried again')
element.send_keys(Keys.RETURN)



# Get Element by ID:
driver.get('https://www.python.org/')
element = driver.find_element_by_id('id-search-field')
time.sleep(1)
element.clear()
element.send_keys('less')
element.send_keys(Keys.RETURN)
driver.quit()

