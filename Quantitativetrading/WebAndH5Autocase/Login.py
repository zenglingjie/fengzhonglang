from selenium import webdriver
import time



chromedriver = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver'

driver = webdriver.Chrome(chromedriver)
driver.get("http://q.tgw360.com/index.html")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginurl"]').click()
driver.find_element_by_xpath('//*[@id="username"]').clear()
driver.find_element_by_xpath('//*[@id="username"]').send_keys('18716361836')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="password"]').clear()
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="login_incont"]/button').click()

