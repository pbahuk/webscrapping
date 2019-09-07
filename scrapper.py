from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.pluralsight.com/')

driver.quit()

# Opening a webpage with options.
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

driver.get("http://www.pluralsight.com/")
driver.quit()

