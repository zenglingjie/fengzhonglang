#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, string
import time
import itertools

chromedriver = 'C:/Program Files/Google/Chrome/Application/chromedriver'#浏览器下载一个google驱动器chromedriver，这是是驱动器的路径

driver = webdriver.Chrome(chromedriver)
driver.get('https://wanwang.aliyun.com/domain/searchresult/')

elem = driver.find_element_by_class_name("ipt-domain ")
elem.clear()


a = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
for i in itertools.product(a, repeat=4):
    # n=random.randint(4,4)
    # s = []
    # for i in range(n):
    #     s.append(random.choice(string.ascii_lowercase))

    elem.send_keys(i)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)

    if driver.find_element_by_xpath(".//*[@id='J_searchResBox']/ul/li[1]/div[1]/span[2]").text == '(未注册)':
        file_object = open('noregister.txt', 'a')
        file_object.write(i.__str__())
        file_object.write("\n")
        file_object.close()
    if driver.find_element_by_xpath(".//*[@id='J_searchResBox']/ul/li[1]/div[1]/span[2]").text == '(查询超时)':
        time.sleep(5)
    elem.clear()
