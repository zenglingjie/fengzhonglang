from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.find_element_by_xpath('/html/body/header/div/div[2]/nav/ul/li[2]/a').click()
driver.find_element_by_xpath('/html/body/header/div/div[2]/nav/ul/li[2]/div/div/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="sname"]').send_keys('test策略')
driver.find_element_by_xpath('//*[@id="li1"]').click()
driver.find_element_by_xpath('//*[@id="ul9"]/li[2]').click()
driver.find_element_by_xpath('//*[@id="li2"]').send_keys('5')
driver.find_element_by_xpath('//*[@id="li3"]').click()
driver.find_element_by_xpath('//*[@id="li4"]').click()
driver.find_element_by_xpath('//*[@id="ul3"]/li[2]').click()
driver.find_element_by_xpath('//*[@id="li6"]').send_keys('2')
driver.find_element_by_xpath('//*[@id="li7"]').send_keys('2')