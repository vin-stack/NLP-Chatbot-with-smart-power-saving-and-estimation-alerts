from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://youtube.com')
searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchbutton.click()